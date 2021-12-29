# Track corpus-related metrics and statistics


def totalcount(body):
    '''
    IN: body: list(str), a list of individual words
    OUT: total: int, the number of total words
    '''
    return len(body)


def unique(body):
    '''
    IN: body: list(str), a list of individual words
    OUT: types: set, the list of unqie words
    '''
    return set(body)


def occurences(body):
    '''
    IN: body: list(str), a list of individual words
    OUT: frequency: int, the number of total words
    '''
    frequency = dict.fromkeys(unique(body), 0)
    for word in body:
        frequency[word] += 1
    return frequency


def ttr(body):
    '''
    IN: body: list(str), a list of individual words
    OUT: types: int, the number of unique types
    OUT: tokens, init, the number of all tokens
    '''
    return len(unique(body)), totalcount(body)
