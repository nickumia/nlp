
import botocore

import nlp.processing.appraisal.dictionary as npad
import nlp.language.focals as nlfo


class TestWordMap():
    @classmethod
    def setup_class(cls):
        try:
            npad.DICTIONARY.restore('dictionary.dump')
        except (FileNotFoundError, botocore.exceptions.ClientError):
            # npad.DICTIONARY.prepopulate(text.words)
            pass

    def test_wordmap_init(self):
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

    def test_wordmap_basic(self):
        A = nlfo.WordMap(['go'])
        A.generateByDefinitions(layers=2)
        A.backup('wordmap.dump')
        npad.DICTIONARY.backup('dictionary.dump')

        pam = A.getMap()
        # print(pam)
        assert len(pam[0]) == 1
        assert len(pam[0]) < len(pam[1])
        assert len(pam[1]) < len(pam[2])

    def test_wordmap_weights(self):
        A = nlfo.WordMap(['go'])
        A.generateByDefinitions(layers=2)
        A.backup('wordmap.dump')
        npad.DICTIONARY.backup('dictionary.dump')

        # pam = A.getMap()
        A.collapse()

        # TODO: add assertions

    def test_wordmap_combine(self):
        A = nlfo.WordMap(['go'])
        B = nlfo.WordMap(['back'])
        A.generateByDefinitions(layers=2)
        B.generateByDefinitions(layers=2)
        npad.DICTIONARY.backup('dictionary.dump')
        A.collapse()
        B.collapse()

        C = nlfo.combineMaps(A, B)
        assert C.map[0] == ['go', 'back']
        for key in A.ranking:
            assert key in C.ranking
        for key in B.ranking:
            assert key in C.ranking
        for key in A.singular:
            assert key in C.singular
        for key in B.singular:
            assert key in C.singular


if __name__ == '__main__':
    print('1 - test_wordmap_init')
    print('2 - test_wordmap_basic')
    print('3 - test_wordmap_weights')
    a = input('Which test to run?')
    z = TestWordMap()

    if a == '1':
        z.test_wordmap_init()
    if a == '2':
        z.test_wordmap_basic()
    if a == '3':
        z.test_wordmap_weights()
