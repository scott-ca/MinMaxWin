# MinMaxWin
A software utility that provides quick access to frequently used applications, facilitating seamless window toggling through shortcut keys.

&nbsp;


# Table of contents
* [Summary](#summary)
* [Roadmap](#roadmap)
* [Installation instructions](#installation-instructions)
* [Running MinMaxWin](#running-minmaxwin)
* [License](#license)

&nbsp;

## Summary

MinMaxWin is a software utility designed to streamline your workflow by providing quick access to your most frequently used application. It eliminates the need to use alt-tab or sift through multiple open applications, allowing you to focus on your work, whether it's Software Development, Graphic Design, Gaming, or even general computer use.

MinMaxWin offers two modes: single-window mode (default) and multiple-window mode. Both modes use the shortcut keys of ctrl + / to capture the active window, and ctrl + ` to toggle the window.

In single-window mode, MinMaxWin minimizes and maximizes the captured window, regardless of whether the window or application is in focus. For example, if you're working on a project and have captured your word processor, you can easily minimize and maximize it without having to search for it among your other open applications.

In multiple-window mode, the captured window or application won't be minimized. Instead, when you use the toggle shortcut key, MinMaxWin temporarily captures the window you're currently using and switches focus to the captured window. When you press the toggle shortcut key again, it returns you to the application you were in when you initially pressed the key combination, regardless of any other applications you've interacted with since then. This allows you to quickly switch back and forth between two applications.

## Roadmap

Below is a list of features currently planned to be added in the future.

- **Cross-platform support:** Currently MinMaxWin is only supported by Linux. We are working on adding support for Windows as well.
- **Multiple window management:** Adding support to allow multiple windows to be toggled each having their own shortcut keys.
- **Custom shortcut keys:**: Adding support for changing the default shortcut keys for capturing the window as well as the shortcut key for toggling the window.

## Installation instructions

This currently is only supported in Linux, however cross-platform support for windows is currently in development.

## Instructions


### Step 1: Clone the MinMaxWin repository

If you have Git installed, open a terminal or command prompt and execute the following command to clone the repository:
```
git clone https://github.com/scott-ca/minmaxwin.git
cd minmaxwin
```
Alternatively, you can manually download the files by clicking the "Code" button at the top right of the webpage and selecting "Download ZIP." Extract the downloaded ZIP file to your chosen directory. Open the command prompt or terminal in the extracted folder.


### Step 2: Setting up the environment

You can utilize the provided installation for a portable version of Miniconda to create an isolated environment named portable_env. This approach eliminates the need for a prior python or conda installations, and and as such won't interfere with any existing installations you may have.

Alternativtly, you can utliize your own python envirioment as long as you have the requirements file installed and run the MinMaxWin.py file directly.


### Prerequisites

If you are on linux, and using X11 you will need to install libxcb-xinerama package, which is required by PySide to manage the GUI interface. This package does need to be locally installed as it is unable to be loaded from the portable environment, and as a result needs to be installed even in the case where you run this from a usb drive.

You can use the appropriate command based on your Linux distribution:

**Debian/Ubuntu:** 
```
sudo apt-get install libxcb-xinerama0
```
**Fedora:** 
```
sudo dnf install libxcb-xinerama
```
**CentOS/RHEL:**
```
sudo yum install libxcb-xinerama
```
**Arch:**
```
sudo pacman -S libxcb
```
**Gentoo:**
```
sudo emerge libxcb
```



### Downloading and configuration of the portable the environment(recommended)

To download the portable Miniconda installer and configure the environment you will need to run the following command in your terminal.

```
./portable_install.sh
```

### Alternative configuration

Alternatively, if you wish to use your own previously installed conda environment or non-conda python environments, you can run MinMaxWin.py directly instead of using the provided scripts, as they launch the script with the assumption of using the portable environment.

If you are using your own installation of Conda/Miniconda
```
create -y MinMaxWin python=3.10.4
pip install -r requirements.txt
python MinMaxWin.py
```


### Additional Customization

### <ins>Basic</ins>

**Auto-start:** If you would like to have MinMaxWin start automatically with your computer you can the commands below in your terminal

```
./linux_startup.sh
```

&nbsp;

This will add MinWinMax to your ~/.config/autorun/ folder allowing it to boot up automatically when you start your computer.


## Running MinMaxWin

To run it silently run the command below in the terminal.


```
./run_linux.sh
```
To run it verbosely run the command below in the terminal. This is useful so you can see messages related to capturing and toggling of the window should you need to do any troubleshooting.

```
./verbose_linux.sh
```

Once it has been loaded you will see the black and white software window icon that will appear in your system tray, typically this is located near the clock at either the top-right or bottom-right corner of your screen.

![icon](https://github.com/scott-ca/MinMaxWin/assets/59944183/1236ecba-3410-4da1-ae81-e46a45122280)

Once the software is loaded, it will launch in single-window mode. When in this mode you can designate your preferred toggle window. Simply select the window and press ctrl + /. After setting this, you can easily toggle between minimizing and maximizing the window using the keyboard shortcut ctrl + ` (backtick), located at the top left of your keyboard.

To enable multiple-window mode, right-click the icon in the system tray and select the option "Multiple-window mode". This option is not enabled by default. 

In multiple-window mode, the captured window or application won't be minimized. Instead, when you use the toggle shortcut key, MinMaxWin temporarily captures the window you're currently using and switches focus to the captured window. When you press the toggle shortcut key again, it returns you to the application you were in when you initially pressed the key combination, regardless of any other applications you've interacted with since then. This allows you to quickly switch back and forth between two applications.

Your mode preference is automatically saved in a file called `settings.json` and is loaded each time the script is launched, ensuring that MinMaxWin remembers your preference.

### Alternative launching of MinMaxWin

Alternatively, if you wish to use your own previously installed conda environment or non-conda python environments, you can run MinMaxWin.py directly instead of using the provided scripts, as they launch the script with the assumption of using the portable environment.

If you are using your own installation of Conda/Miniconda
```
python MinMaxWin.py
```
&nbsp;
&nbsp;

## Feedback
I am happy to hear any feedback including but not limited to any features that you may like to see added. I won't make any commitments to add any of the features, however I will review them and should time allow see which features I may be able to implement.

## License

MinMaxWin is licensed with a MIT License, in short this means that it can be used by anyone for any purpose. 

**Permissions:**
- Commercial use: You may use the software for commercial purposes.
- Modification: You may make changes to the software.
- Distribution: You may distribute the software.
- Private use: You may use the software for private purposes.

**Conditions:**
- License and copyright notice: You must include the original copyright notice and the license.

**Limitations:**
- Liability: The license includes a disclaimer of liability.
- Warranty: The software is provided without warranty.

For the exact terms and conditions of the license, please see the [LICENSE](LICENSE) file in the repository.
