# ctci 5.4

def setBit(n, i):
    return n | (1 << i)

def clearBit(n, i):
    return n & ~(1 << i)

def getBit(n, i):
    return (n & (1 << i)) != 0

def smallerLarger(n):
    moveSmallFr, moveLargeTo, i = None, None, 0
    while i < 32 and (moveSmallFr == None or moveLargeTo == None):
        ith, inext = getBit(n, i), getBit(n, i + 1)
        if ith and not inext and not moveLargeTo:
            moveLargeTo = i + 1
        elif not ith and inext and not moveSmallFr:
            moveSmallFr = i + 1
        i += 1
    print('Smaller: {}'.format(clearBit(setBit(n, moveSmallFr - 1), moveSmallFr)))
    print('Larger:  {}'.format(clearBit(setBit(n, moveLargeTo), moveLargeTo - 1)))

smallerLarger(20)
smallerLarger(12)