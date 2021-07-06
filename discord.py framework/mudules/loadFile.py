import pickle


def loadFile(path):
    "loads file saven in binary form"
    f = open(path, "rb")
    file = pickle.load(f)
    f.close()
    return file
