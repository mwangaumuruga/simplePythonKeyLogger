# simplePythonKeyLogger
Keylogger

A simple Python-based keylogger that records keystrokes to a file on your Desktop.
Table of Contents

    Overview
    Requirements
    Setup and Installation
    Usage
    Note on Ethics and Privacy

Overview

This keylogger project is a basic tool that uses Python to log each key pressed on the keyboard. The recorded keystrokes are saved to a file called keylog.txt on your Desktop.

Please note: This program is intended for educational purposes only. Make sure to use it responsibly and legally.
Requirements

    Python 3.6 or higher
    pynput library for Python

Setup and Installation

    Clone or Download the Project
        Clone this repository to your local machine, or download the keylogger.py file directly.

    Install Python
        Make sure Python is installed on your system. You can download Python from here.

    Install Required Packages
        Open a terminal (or Command Prompt on Windows) and install pynput by running:

        bash

        pip install pynput

Usage

    Configure the Script (optional):
        By default, the keystrokes will be saved to a file on your Desktop named keylog.txt. If you want to change the save location, update the log_dir variable in keylogger.py.

    Run the Keylogger:
        Linux/Mac:

        bash

python3 keylogger.py

Windows: Run the script as an administrator to ensure it can capture all keystrokes:

cmd

    python keylogger.py

Stop the Keylogger:

    To stop logging, you can manually close the terminal or Command Prompt running the script.

View Keystrokes:

    Open the keylog.txt file on your Desktop to see the recorded keystrokes.
