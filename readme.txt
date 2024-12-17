Description

This script is a basic keylogger implemented in Python. It uses the pynput library to capture keystrokes and writes them to a log file (keyfile.txt). The script is designed for academic purposes, such as learning about Python programming, event listeners, and file handling.

DISCLAIMER: This script is intended solely for educational and testing purposes in controlled environments. Unauthorized use of keyloggers to capture data without explicit consent is unethical and illegal. The author does not condone or encourage misuse of this code.

Features

Logs alphanumeric keys and special keys (e.g., Space, Enter, Backspace) to a file.

Creates a keyfile.txt log file in the working directory.

Flushes data to the log file in real-time to ensure consistent logging.

Stops execution when the ESC key is pressed.

Prerequisites

Python 3.7 or later

pynput library