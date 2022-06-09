import socket
import cv2
import numpy as np
import pyautogui
import time


SCREEN_SIZE = pyautogui.size()


def restart():
    print("\n\n")
    time.sleep(1)
    s = socket.socket()
    port = 8080
    s.bind(('', port))
    print("Waiting for connections...")
    s.listen()
    conn, addr = s.accept()
    print(addr, "is connected to the server")
    targetname = conn.recv(1024).decode()
    print("Host name is: " + targetname.split("|")[0])
    print("Press 'q' to change computers")
    while True:
        try:
            data = conn.recv(2**23)
            ndata = np.frombuffer(data, np.uint8)
            if ndata.size != int(targetname.split("|")[-1].split(",")[-1]) * int(targetname.split("|")[-1].split(",")[0]) * 3:
                continue
            frame = np.reshape(ndata, (int(targetname.split("|")[-1].split(",")[-1]), int(targetname.split("|")[-1].split(",")[0]), 3))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (int((int(targetname.split("|")[-1].split(",")[0])/5)*4), int((int(targetname.split("|")[-1].split(",")[-1])/5)*4)))
            cv2.imshow(targetname.split("|")[0], frame)
            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()
                conn.close()
                s.close()
                restart()
                return
        except Exception as e:
            print(e)
            cv2.destroyAllWindows()
            conn.close()
            s.close()
            restart()
            return

restart()