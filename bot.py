import os
import win32gui
import time
import PIL
import threading
import random
from pynput.keyboard import Key, Controller


keyboard = Controller()
lock = threading.Lock()

global handlers
handlers = []


def openFile():
    try:
        os.startfile('C:\\WINDOWS\\system32\\notepad.exe')
        print("Starting program...")
    except Exception as e:
        print(str(e))

def selectingActiveWindow(activewindowhandler):           
    win32gui.SetForegroundWindow(activewindowhandler)

def typing(role):
    if role == 'Main':
        selectingActiveWindow(handlers[0])
        keyboard.press('A')
        keyboard.release('A')
        print('Main act')
        
    elif role == 'sup':
        selectingActiveWindow(handlers[1])
        keyboard.press('W')
        keyboard.release('W')
        print('Sup act')

    else:
        print ('Role not slected!')

def window_setup():
    time.sleep(3)
        
    def enumHandler(hwnd, handlers):
        if win32gui.IsWindowVisible(hwnd):
            if 'Notepad' in win32gui.GetWindowText(hwnd):
                handlers.append (hwnd)
                    
                if len(handlers) > 1:
                        win32gui.MoveWindow(handlers[0], 0, 0, 699, 1030, True)
                        win32gui.MoveWindow(handlers[1], 700, 0, 699, 1030, True)
                        #win32gui.MoveWindow(handlers[0], 0, 0, 1600, 1030, True)
                        #win32gui.MoveWindow(handlers[1], 0, 0, 1600, 1030, True)

            if 'Python' in win32gui.GetWindowText(hwnd):
                    win32gui.MoveWindow(hwnd, 1400, 0, 520, 1030, True)


    win32gui.EnumWindows(enumHandler, handlers)


                    
def setup():
    for j in range (1,3):
        openFile()
    window_setup()

setup()


def mainThread():
    while True:
        with lock:
            typing('Main')
        time.sleep(random.uniform(3.0,5.0))
    
def supportThread():
    while True:
        with lock:
            typing('Sup')
        time.sleep(random.uniform(1080.0,1100.0))

def threader(threadNumber, name):
    print(threadNumber)
    if threadNumber == 1:
        mainThread()
    elif threadNumber == 2:
        supportThread()
    else:
        print('threadNumber oolist?')


t1 = threading.Thread(target = threader, name = 'Mainthread', args = (1, 'Mainthread'))
t1.start()

t2 = threading.Thread(target = threader, name = 'Supthread', args = (2, 'Supthread'))
t2.start()



    




