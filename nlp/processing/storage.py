
import pickle


class Storage():
    def __init__(self):
        self.save = None

    def restore(self, filename):
        '''
        IN: filename, str: File that has stored state of dictionary
        '''
        with open(filename, 'rb') as intar:
            self.save = pickle.load(intar)

    def backup(self, filename):
        '''
        IN: filename, str: File to store dictionary in
        '''
        with open(filename, 'wb') as outar:
            pickle.dump(self.save, outar,
                        protocol=pickle.HIGHEST_PROTOCOL)
