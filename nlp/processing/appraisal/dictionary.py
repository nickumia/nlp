# This is the integration with web-search-dictionary

import websearchdict


class LocalDictionary():
    def __init__(self):
        self.dictionary = {}

    def prepopulate(self, words):
        '''
        IN: words, list: A list of words to lookup
        '''
        for word in words:
            if word not in self.dictionary:
                self.dictionary[word] = websearchdict.lookup(word)

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
