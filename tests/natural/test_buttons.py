
import botocore

import nlp.processing.appraisal.dictionary as npad
import nlp.language.focals as nlfo
import nlp.natural.buttons as nnb


def test_buttons_bias_different():
    ''' Test that internal/external bias computation words '''
    try:
        npad.DICTIONARY.restore('dictionary.dump')
    except (FileNotFoundError, botocore.exceptions.ClientError):
        pass

    left = nlfo.WordMap(['left'])
    right = nlfo.WordMap(['right'])

    left.generateByDefinitions(layers=2)
    right.generateByDefinitions(layers=2)
    npad.DICTIONARY.backup('dictionary.dump')
    left.collapse()
    right.collapse()

    model = nnb.Buttons(brain=left, pinky=right)
    model.intersect()
    c, i = model.bias()
    assert c > i
    # The following assertions are based on my hypothesis, it's not required
    # assert c > 0.5
    # assert i < 0.5


def test_buttons_match_different():
    ''' Test that internal/external bias computation words '''
    try:
        npad.DICTIONARY.restore('dictionary.dump')
    except (FileNotFoundError, botocore.exceptions.ClientError):
        pass

    left = nlfo.WordMap(['left'])
    right = nlfo.WordMap(['right'])

    left.generateByDefinitions(layers=2)
    right.generateByDefinitions(layers=2)
    npad.DICTIONARY.backup('dictionary.dump')
    left.collapse()
    right.collapse()

    model = nnb.Buttons(brain=left, pinky=right)
    model.intersect()
    similar = model.match()
    assert similar < 0.6


def test_buttons_bias_similar():
    ''' Test that internal/external bias computation words '''
    try:
        npad.DICTIONARY.restore('dictionary.dump')
    except (FileNotFoundError, botocore.exceptions.ClientError):
        pass

    left = nlfo.WordMap(['operate'])
    right = nlfo.WordMap(['drive'])

    left.generateByDefinitions(layers=2)
    right.generateByDefinitions(layers=2)
    npad.DICTIONARY.backup('dictionary.dump')
    left.collapse()
    right.collapse()

    model = nnb.Buttons(brain=left, pinky=right)
    model.intersect()
    c, i = model.bias()
    assert 0.4 < c < 0.6
    assert 0.4 < i < 0.6


def test_buttons_match_similar():
    ''' Test that internal/external bias computation words '''
    try:
        npad.DICTIONARY.restore('dictionary.dump')
    except (FileNotFoundError, botocore.exceptions.ClientError):
        pass

    left = nlfo.WordMap(['operate'])
    right = nlfo.WordMap(['drive'])

    left.generateByDefinitions(layers=2)
    right.generateByDefinitions(layers=2)
    npad.DICTIONARY.backup('dictionary.dump')
    left.collapse()
    right.collapse()

    model = nnb.Buttons(brain=left, pinky=right)
    model.intersect()
    similar = model.match()
    assert similar > 0.6
