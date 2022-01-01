
def sanitize(word):
    return lowercase(word)


def lowercase(word):
    return word.lower()


def sortabasedonb(a):
    # new = zip(a, b); new.sort(); zip(*new)
    na, nb = zip(*sorted(zip(a[0], a[1])))
    # return(na,nb)
    return (list(na), list(nb))


def combineLikeValues(a):
    # TODO: figure out what this does
    x = a[1]
    y = a[0]

    for i, z in enumerate(x):
        if i > 0 and z == x[i-1]:
            return combineLikeValues([y[0:i-1] + [y[i] + y[i-1]] + y[i+1:],
                                      x[0:i] + x[i+1:]
                                      ])
    return y, x
