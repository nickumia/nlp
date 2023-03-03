
import nlp.processing.corpus.identity as npci
import nlp.processing.appraisal.basic_text as npab
import nlp.processing.filters as npf


class BasicText():

    def __init__(self, original):
        self.text = original
        self.groups = npci.group(npf.semi_sanitize(original))
        self.words = [npf.lowercase(i) for i in self.groups[npci.WORDS]]
        self.contexts = npab.generate(self.groups, npf.semi_sanitize(original))

    def getWords(self):
        return self.words
