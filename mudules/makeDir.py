import os


def makeDir(path):
    "makes directory if not existant"
    if not os.path.exists(path):
        os.makedirs(path)
