# Track corpus-related metrics and statistics

from nlp.processing.filters import sanitize

def ttr(body):
    '''
    IN: body: list(str), a list of individual words
    OUT: types: int, the number of unique types
    OUT: tokens, init, the number of all tokens
    '''
    types = {}

    for word in body:
        word = sanitize(word)
        if word in types.keys():
            types[word] += 1
        else:
            types[word] = 0
    return len(types.keys()), len(body)
