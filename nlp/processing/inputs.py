
import nlp.processing.corpus.identity as npci
import nlp.processing.appraisal.basic_text as npab


class BasicText():

    def __init__(self, original):
        self.text = original
        self.words = original.split(" ")
        self.groups = npci.group(original)
        self.contexts = npab.generate(self.groups, original)

    def getWords(self):
        return self.words
