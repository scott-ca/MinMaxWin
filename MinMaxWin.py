import setproctitle
setproctitle.setproctitle('MinMaxWin')
from pynput import keyboard
import subprocess
import platform
import sys
from PySide2.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PySide2.QtGui import QIcon
from threading import Thread
import json

def load_settings():
    """
    Load settings from a JSON file.
    """
    try:
        with open("settings.json", "r") as file:
            settings = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        settings = {"multiwin_mode": False}  # Default settings
    return settings

def save_settings(settings):
    """
    Save settings to a JSON file.
    """
    with open("settings.json", "w") as file:
        json.dump(settings, file)

class KeyPressListener:
    """
    A class to listen for specific key presses and perform their respections actions for that key combinations.
    """

    def __init__(self):
         # Initialize with the control key not pressed, no window captured, and assuming the window is maximized, settings loaded from settings.json

        settings = load_settings()
        self.ctrl_pressed = False
        self.captured_window = None
        self.temporarily_captured_window = None
        self.window_state = 'maximized'
        self.multiwin_mode = settings.get("multiwin_mode", False)
        self.singlewin_mode = not settings.get("multiwin_mode", False)

    def on_press(self, key):
        """
        Handle actions when a key is pressed. Specifically, it listens for Ctrl, `/`, and '`' key presses.
        """

        if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
            self.ctrl_pressed = True

        # Capture the active window if '/' is pressed while Ctrl is held down and if so capture the active window
        elif key == keyboard.KeyCode.from_char('/') and self.ctrl_pressed:
            self.capture_active_window()

        # Toggle the window state if '`' is pressed while Ctrl is held down and if so toggling the window state
        elif key == keyboard.KeyCode.from_char('`') and self.ctrl_pressed:
            self.toggle_window_state()

    def on_release(self, key):
        """
        Resets the ctrl_pressed flag when either control key is released.
        """

        if key in [keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
            self.ctrl_pressed = False

    def capture_active_window(self):
        """
        Captures the currently active window using system-specific commands.
        """
        
        if platform.system() == "Linux":
            self.captured_window = subprocess.check_output(["xdotool", "getactivewindow"]).strip().decode()
            print(f"Captured Window ID: {self.captured_window}")
        elif platform.system() == "Windows":
            print("Windows compatibility not implemented yet. It will be implemented in a future update .")
            pass  # Windows-specific implementation

    def toggle_window_state(self):
        """
        Toggles the state of the captured window between minimized and maximized. 
        
        Modifies the window toggling behavior based on the singlewin_mode and multiwin_mode values .
        """
        # If multiwin_mode is enabled, switch focus between the captured window and the temporarily captured window
        if self.multiwin_mode:
            if self.window_state == 'maximized':
                # Save the currently focused window before switching
                try:
                    self.temporarily_captured_window = subprocess.check_output(["xdotool", "getwindowfocus"]).strip().decode()
                    print(f"Temporarily storing window: {self.temporarily_captured_window}")
                except subprocess.CalledProcessError as e:
                    print(f"Error capturing temporarily focused window: {e}")
                # Activate the captured window without maximizing
                try:
                    subprocess.run(["xdotool", "windowactivate", self.captured_window])
                    self.window_state = 'minimized'
                    print(f"Switched focus to captured window: {self.captured_window}")
                except subprocess.CalledProcessError as e:
                    print(f"Error activating captured window: {e}")
            else:
                # Switch focus back to the temporarily captured window
                if self.temporarily_captured_window:
                    try:
                        subprocess.run(["xdotool", "windowactivate", self.temporarily_captured_window])
                        print(f"Switched focus back to temporarily stored window: {self.temporarily_captured_window}")
                    except subprocess.CalledProcessError as e:
                        print(f"Error reactivating temporarily stored window: {e}")
                self.window_state = 'maximized'
        else:
            # If the singlewin_mode is enabled, toggle the state of the captured window
            if platform.system() == "Linux" and self.captured_window:
                if self.window_state == 'maximized':
                    try:
                        subprocess.run(["xdotool", "windowminimize", self.captured_window])
                        self.window_state = 'minimized'
                        print(f"Minimized window: {self.captured_window}")
                    except subprocess.CalledProcessError as e:
                        print(f"Error minimizing window: {e}")
                else:
                    try:
                        subprocess.run(["xdotool", "windowactivate", self.captured_window])
                        self.window_state = 'maximized'
                        print(f"Maximized window: {self.captured_window}")
                    except subprocess.CalledProcessError as e:
                        print(f"Error maximizing window: {e}")
            elif platform.system() == "Windows":
                pass  # Placeholder for Windows-specific implementation
           
def create_tray_icon(listener):
    app = QApplication(sys.argv)
    tray_icon = QSystemTrayIcon(QIcon("icon.png"), app)
    menu = QMenu()

    # Nested function to handle exit operation
    def exit_application():
        save_settings({"multiwin_mode": listener.multiwin_mode})
        app.quit()

    # Add an "Exit" action to the menu
    exit_action = QAction("Exit")
    exit_action.triggered.connect(exit_application)
    menu.addAction(exit_action)

    # Single-window mode toggle action
    singlewin_mode_action = QAction("Single-window mode", app)
    singlewin_mode_action.setCheckable(True)  # Make the singlewin_mode action checkable

    # Set the checkmark based on the loaded settings
    singlewin_mode_action.setChecked(listener.singlewin_mode)

    singlewin_mode_action.triggered.connect(lambda checked: (
        setattr(listener, 'singlewin_mode', checked),
        setattr(listener, 'multiwin_mode', not checked),  # Disable multi-switch mode when single-window mode is enabled
        multiwin_mode_action.setChecked(not checked),  # Update the checkmark for the multiple-window mode action
        print("Single-window mode enabled" if checked else "Single-window mode disabled"),
        save_settings({"multiwin_mode": not checked})  # Save settings when changed
    ))
    menu.addAction(singlewin_mode_action)

    # Multi-switch toggle action
    multiwin_mode_action = QAction("Multiple-window mode", app)
    multiwin_mode_action.setCheckable(True)  # Update the checkmark for the multiple-window mode action

    # Set the checkmark based on the loaded settings
    multiwin_mode_action.setChecked(listener.multiwin_mode)

    multiwin_mode_action.triggered.connect(lambda checked: (
        setattr(listener, 'multiwin_mode', checked),
        setattr(listener, 'singlewin_mode', not checked),  # Disable single-window mode when multiple-window mode is enabled
        singlewin_mode_action.setChecked(not checked),  # Update the checkmark for the single-window mode action
        print("Multiple-window enabled" if checked else "Multiple-window disabled"),
        save_settings({"multiwin_mode": checked})  # Save settings when changed
    ))
    menu.addAction(multiwin_mode_action)

    tray_icon.setContextMenu(menu)
    tray_icon.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    # Initialize the key press listener
    listener = KeyPressListener()
    
    # Start the key press listener in a separate thread
    listener_thread = Thread(target=lambda: keyboard.Listener(on_press=listener.on_press, on_release=listener.on_release).start(), daemon=True)
    listener_thread.start()

    # Create and display the system tray icon with the listener passed as an argument
    create_tray_icon(listener)
