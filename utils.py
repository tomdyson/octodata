import os


def debug(str):
    if os.getenv("DEBUG", "").lower() in ["true", "1"]:
        print(str)
