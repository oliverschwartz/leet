import random

def pythag_triples(l):

    cs = set()
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                cs.add(l[i] ** 2 + l[j] ** 2)

    for e in l:
        if e ** 2 in cs:
            return True
    return False

assert not pythag_triples([1, 2, 3])
assert pythag_triples([3, 4, 5])

