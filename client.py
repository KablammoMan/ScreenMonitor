import socket
import time
import numpy as np
import pyautogui
import ctypes


SCREEN_SIZE = pyautogui.size()
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

def next():
    print("Waiting 5s")
    time.sleep(5)
    restart()


def restart():
    s = socket.socket()
    host = "S20364-PC"
    hostname = socket.gethostname()
    port = 8080
    connected = False
    while not connected:
        try:
            s.connect((host, port))
            connected = True
        except Exception as e:
            connected = False
    s.send((hostname + "|" + str(SCREEN_SIZE[0]) + "," + str(SCREEN_SIZE[1])).encode())
    while True:
        img = pyautogui.screenshot(region=(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))
        frame = np.array(img)
        try:
            s.send(frame.tobytes())
        except Exception as e:
            print(e)
            s.close()
            next()
            return
restart()