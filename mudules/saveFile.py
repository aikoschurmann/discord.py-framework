import pickle


def saveFile(path, data):
    "saves data to path in binary form"
    f = open(path, "wb")
    pickle.dump(data, f)
    f.close()
