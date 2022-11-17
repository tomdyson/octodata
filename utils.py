import os


def debug(str):
    if os.getenv("DEBUG", False):
        print(str)
