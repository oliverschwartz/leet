"""Some reference implementations of bit methods described in CTCI"""

# get the ith bit of n
def getBit(n, i):
    mask = 1 << i
    return (mask & n) != 0

assert(getBit(0, 0) == False)
assert(getBit(8, 3) == True)
assert(getBit(7, 2) == True)

# set the ith bit of n to 1
def setBit(n, i):
    mask = 1 << i
    return mask | n

assert(setBit(3, 2) == 7)
assert(setBit(0, 3) == 8)
assert(setBit(16, 4) == 16)

# clear the ith bit of n
def clearBit(n, i):
    mask = ~(1 << i)
    return (mask & n)

assert(clearBit(16, 4) == 0)
assert(clearBit(7, 1) == 5)
assert(clearBit(8, 0) == 8)

# set the value of the ith bit to v
def updateBit(n, i, v):
    if v == 1:
        return setBit(n, i)
    if v == 0:
        return clearBit(n, i)

assert(updateBit(8, 3, False) == 0)
assert(updateBit(7, 3, True) == 15)
