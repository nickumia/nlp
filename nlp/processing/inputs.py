
class BasicText():

    def __init__(self, original):
        self.text = original
        self.words = original.split(" ")

    def getWords(self):
        return self.words
