

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
