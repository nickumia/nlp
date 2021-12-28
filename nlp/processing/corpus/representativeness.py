# Track corpus-related metrics and statistics


def ttr(body):
    '''
    IN: body: list(str), a list of individual words
    OUT: types: int, the number of unique types
    OUT: tokens, init, the number of all tokens
    '''
    return len(set(body)), len(body)
