
import botocore

import nlp.processing.appraisal.dictionary as npad
import nlp.language.focals as nlfo
import nlp.natural.buttons as nnb

move = ['go', 'move', 'drive', 'walk', 'advance']
stop = ['stop', 'pause', 'cease', 'yield']

left = ['left']
up = ['up']
down = ['down']
right = ['right']

SAVED_DICTIONARY = 'dictionary.dump'

try:
    npad.DICTIONARY.restore(SAVED_DICTIONARY)
except (FileNotFoundError, botocore.exceptions.ClientError):
    starting_words = move + stop + left + up + down + right
    npad.DICTIONARY.prepopulate(starting_words)

MODEL = {
    'move': nlfo.WordMap(move),
    'stop': nlfo.WordMap(stop),
    'left': nlfo.WordMap(left),
    'up': nlfo.WordMap(up),
    'down': nlfo.WordMap(down),
    'right': nlfo.WordMap(right)
}

for key in MODEL.keys():
    original_dictionary = npad.DICTIONARY.dictionary
    MODEL[key].generateByDefinitions(layers=2)
    if npad.DICTIONARY.dictionary != original_dictionary:
        npad.DICTIONARY.backup(SAVED_DICTIONARY)
    MODEL[key].collapse()


def evaluate(known, unknown):
    tester = nnb.Buttons(brain=known, pinky=unknown)
    tester.intersect()
    return tester.match()
