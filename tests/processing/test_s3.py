
import nlp.processing.storage as nps


def test_basic_upload_download():
    tester = nps.S3Storage('nlpdev', 'nlpdev')
    original = {1: 'an important opbject'}

    tester.save = original
    tester.backup('test')
    tester.save = {}
    tester.restore('test')

    assert tester.save == original
