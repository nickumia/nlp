
import nlp.processing.appraisal.dictionary as npad
import nlp.language.focals as nlfo


def test_wordmap_init():
    original = ['test']
    temp = ['test', 'what']
    A = nlfo.WordMap(original)
    save_file = 'wordmap.dump'

    assert A.getMap() == {0: original}

    A.backup(save_file)
    A.map = {0: temp}
    assert A.getMap() == {0: temp}

    A.restore(save_file)
    assert A.getMap() == {0: original}


def test_wordmap_basic():
    try:
        npad.DICTIONARY.restore('dictionary.dump')
    except FileNotFoundError:
        # npad.DICTIONARY.prepopulate(text.words)
        pass

    A = nlfo.WordMap(['go'])
    A.generateByDefinitions(layers=2)
    A.backup('wordmap.dump')
    npad.DICTIONARY.backup('dictionary.dump')

    # print(A.getMap())
    assert len(A[0]) == 1
    assert len(A[0]) < len(A[1])
    assert len(A[1]) < len(A[2])


if __name__ == '__main__':
    print('1 - test_wordmap_init')
    print('2 - test_wordmap_basic')
    a = input('Which test to run?')

    if a == '1':
        test_wordmap_init()
    if a == '2':
        test_wordmap_basic()
