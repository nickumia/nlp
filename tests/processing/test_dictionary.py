
import nlp.processing.appraisal.dictionary as npad


def test_dictionary_init():
    assert npad.LocalDictionary().dictionary == {}


def test_dictionary_backup_restore():
    original = {'__test__': 'nothing'}
    npad.DICTIONARY.dictionary = original
    npad.DICTIONARY.backup('test.dump')
    npad.DICTIONARY.restore('test.dump')

    assert original == npad.DICTIONARY.dictionary


def test_dictionary_lookup():
    npad.DICTIONARY = npad.LocalDictionary()
    npad.DICTIONARY.lookup('unknown')

    assert 'unknown' in npad.DICTIONARY.dictionary


def test_dictionary_numberOfSenses_wo_prior_lookup():
    npad.DICTIONARY = npad.LocalDictionary()
    assert 8 <= npad.DICTIONARY.numberOfSenses('test') <= 12

# npad.DICTIONARY.restore('dictionary.dump')
# print(len(npad.DICTIONARY.dictionary))
# assert False
