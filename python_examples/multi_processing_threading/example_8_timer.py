import os
import threading


def exec_watcher():
    timer = threading.Timer(5.0, print_files)
    timer.start()


def print_files():
    for i in os.listdir('.'):
        print(i)
    print('*' * 30)
    exec_watcher()


exec_watcher()
