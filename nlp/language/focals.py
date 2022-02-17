
import nlp.processing.appraisal.dictionary as npad
import nlp.processing.corpus.identity as npci
import nlp.processing.storage as nps
import nlp.language.fuzzy as nlf
import nlp.language.constants as nlc


class WordMap(nps.Storage):
    def __init__(self, focal):
        '''
        focal, list: list of words as focal point
        '''
        super().__init__()
        self.focal = focal
        self.map = {0: focal}

    def generateByDefinitions(self, layers=2):

        for layer in range(layers):
            all_words = []
            for word in self.map[layer]:
                entry = npad.DICTIONARY.lookup(word)
                for key, sense in entry.getDefinitions().items():
                    temp_words = npci.group(sense['definition'],
                                            specific=npci.char_word)
                    pos = nlf.posTag(temp_words, whole=True)
                    for item in pos:
                        if item[1] in nlc.CONTENT_WORDS:
                            all_words += [item[0]]
            self.map[layer+1] = all_words

    def backup(self, filename):
        self.save = self.map
        super().backup(filename)

    def restore(self, filename):
        super().restore(filename)
        self.map = self.save

    def getMap(self):
        return self.map