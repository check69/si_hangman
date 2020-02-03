import json
import platform
import os
import random


def read_json(path):
    with open(path, 'rb') as json_file:
        return json.load(json_file)


def clear_screen():
    clean = {"Windows": "cls", "Darwin": "clear", "Linux": "clear"}
    os.system(clean[platform.system()])


def get_key():
    try:
        from msvcrt import getch
        key = getch()
        key = str(key.lower(), "utf-8")
        return key

    except ImportError:
        import termios
        import fcntl
        import sys
        import os

        def kbhit():
            fd = sys.stdin.fileno()
            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
            try:
                while True:
                    try:
                        c = sys.stdin.read(1)
                        return c
                    except IOError:
                        return None
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
                fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

        return kbhit()


def get_random_number(init_number: int, last_number: int) -> int:
    random.seed()
    return random.randint(init_number, last_number)
