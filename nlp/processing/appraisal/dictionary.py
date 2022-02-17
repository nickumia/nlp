# This is the integration with web-search-dictionary

import time
import websearchdict

import nlp.processing.storage as nps
import nlp.processing.interaction.text as npit


class LocalDictionary(nps.Storage):
    def __init__(self, delay=0.5):
        super().__init__()
        self.dictionary = {}
        self.lookup_delay = delay

    def prepopulate(self, words, max_age=2678400):
        '''
        IN: words, list: A list of words to lookup
        '''
        total = len(words)
        for i,word in enumerate(words):
            if word not in self.dictionary:
                npit.progress('Looking up [%d/%d]: %s' % (i, total, word))
                time.sleep(self.lookup_delay)
                self.lookup(word, max_age=max_age)

    def backup(self, filename):
        self.save = self.dictionary
        super().backup(filename)

    def restore(self, filename):
        super().restore(filename)
        self.dictionary = self.save

    def lookup(self, word, max_age=2678400):
        '''
        IN: word, str: Word to lookup
        OUT: dict{pos, definition(str)}

        If word definition is too old, lookup again
            31 days: 2678400s
            90 days: 7776000s
            180 days: 15552000s
        '''
        try:
            result = self.dictionary[word]
            if time.time() - result['timestamp'] > max_age:
                time.sleep(lookup_delay)
                self.dictionary[word] = {
                    'entry': websearchdict.lookup(word),
                    'timestamp': time.time()
                }
            return self.dictionary[word]
        except KeyError:
            time.sleep(lookup_delay)
            self.dictionary[word] = {
                'entry': websearchdict.lookup(word),
                'timestamp': time.time()
            }
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
