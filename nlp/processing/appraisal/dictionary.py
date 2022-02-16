# This is the integration with web-search-dictionary

import websearchdict

import nlp.processing.storage as nps


class LocalDictionary(nps.Storage):
    def __init__(self):
        super().__init__()
        self.dictionary = {}

    def prepopulate(self, words):
        '''
        IN: words, list: A list of words to lookup
        '''
        for word in words:
            if word not in self.dictionary:
                self.dictionary[word] = websearchdict.lookup(word)

    def backup(self, filename):
        self.save = self.dictionary
        super().backup(filename)

    def restore(self, filename):
        super().restore(filename)
        self.dictionary = self.save

    def lookup(self, word):
        '''
        IN: word, str: Word to lookup
        OUT: dict{pos, definition(str)}
        '''
        try:
            return self.dictionary[word]
        except KeyError:
            self.dictionary[word] = websearchdict.lookup(word)
            return self.dictionary[word]

    def numberOfSenses(self, word):
        '''
        IN: word, str: Word to lookup
        OUT: int: the number of known senses of word
        '''
        try:
            return len(self.dictionary[word].getDefinitions())
        except KeyError:
            self.lookup(word)
            return len(self.dictionary[word].getDefinitions())


DICTIONARY = LocalDictionary()
