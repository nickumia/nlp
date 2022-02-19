
from model import MODEL, evaluate, SAVED_DICTIONARY

import nlp.processing.appraisal.dictionary as npad
from nlp.processing.inputs import BasicText
from nlp.language.focals import WordMap, combineMaps


if __name__ == '__main__':
    while True:
        command = input('Enter a phrase to inspect>> ')
        if command == 'q':
            break
        flattened = None
        for word in BasicText(command).getWords():
            new = WordMap([word])
            new.generateByDefinitions(layers=2)
            new.collapse()
            npad.DICTIONARY.backup(SAVED_DICTIONARY)
            if flattened is not None:
                flattened = combineMaps(flattened, new)
            else:
                flattened = new

        results = {}
        for key_word in MODEL.keys():
            results[key_word] = evaluate(MODEL[key_word], flattened)
            print("I'm confident you meant __%s__ by %f" % (key_word,
                                                            results[key_word]))

