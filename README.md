# ScreenMonitor
Uses pyautogui screenshots to send screen data to you over socket. ONLY WORKS WHEN YOU ARE ON THE SAME NETWORK

# Prerequisites: Pip Installs

`client.py`:
- numpy
- pyautogui

`master.py`:
- numpy
- opencv-python

Install the appropriate packages based on the script on the computer

# Prerequisites: Changing Hostname

The hostname in `client.py` (line 20: `host = <YOUR-HOSTNAME>`) must be changed to the hostname of the computer with the `master.py` script. This can be found by running:
```
import socket
print(socket.gethostname())
```
