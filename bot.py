import os
import win32gui
import time
import threading
import random
from pynput.keyboard import Controller

keyboard = Controller()
lock = threading.Lock()


handlers = []


def open_file():
    try:
        os.startfile('C:\\WINDOWS\\system32\\notepad.exe')
        print("Starting program...")
    except Exception as e:
        print(str(e))


def select_active_window(active_window_handler):
    win32gui.SetForegroundWindow(active_window_handler)


def typing(role):
    if role == 'Main':
        select_active_window(handlers[0])
        keyboard.press('A')
        keyboard.release('A')
        print('Main act')

    elif role == 'Sup':
        select_active_window(handlers[1])
        keyboard.press('W')
        keyboard.release('W')
        print('Sup act')

    else:
        print('Role not selected!')


def window_setup():
    time.sleep(3)

    def enum_handler(hwnd, handle):
        if win32gui.IsWindowVisible(hwnd):
            if 'Notepad' in win32gui.GetWindowText(hwnd):
                handle.append(hwnd)
                if len(handle) > 1:
                    win32gui.MoveWindow(handle[0], 0, 0, 499, 1030, True)
                    win32gui.MoveWindow(handle[1], 500, 0, 499, 1030, True)

            if 'Python' in win32gui.GetWindowText(hwnd):
                win32gui.MoveWindow(hwnd, 1400, 0, 520, 1030, True)

    win32gui.EnumWindows(enum_handler, handlers)


def setup():
    for j in range(1, 3):
        open_file()
    window_setup()


setup()


def main_thread():
    while True:
        with lock:
            typing('Main')
        time.sleep(random.uniform(1.0, 3.0))


def support_thread():
    while True:
        with lock:
            typing('Sup')
        time.sleep(random.uniform(2.0, 3.0))


def threader(thread_number, name):
    print(thread_number, name)
    if thread_number == 1:
        main_thread()
    elif thread_number == 2:
        support_thread()
    else:
        print('thread_number out of list?')


t1 = threading.Thread(target=threader, name='Mainthread', args=(1, 'Mainthread'))
t1.start()

t2 = threading.Thread(target=threader, name='Supthread', args=(2, 'Supthread'))
t2.start()
