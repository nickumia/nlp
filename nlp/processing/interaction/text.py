
import sys


def terminal_yes_no(question):
    '''
    IN: question, str, to ask the user
    OUT: bool, yes or no
    '''
    a = input(question)
    if a == 'y':
        return True
    else:
        return False


def load_plain_text(filename, encoding='utf8'):
    '''
    IN: filename, str, name of file to load
    IN: encoding, str, type of file encoding
    OUT: str, the entire body of plaintext
    '''
    with open(filename, "r", encoding=encoding, errors='ignore') as intar:
        lines = intar.readlines()

    temp = " ".join(lines).replace('\n', '')
    return temp


def progress(string):
    sys.stdout.write('\b'*80)
    sys.stdout.write('%s\r' % string)
    sys.stdout.flush()
