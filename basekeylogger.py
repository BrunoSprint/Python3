import pyautogui
import time

def keylogger():
    while True:
        key = pyautogui.press()
        print("Key pressed:", key)
        time.sleep(1)

keylogger() 