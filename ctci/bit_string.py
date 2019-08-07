def bitString(n):
    s = ''
    for i in range(31, -1, -1):
        s += '1' if ((1 << i) & n) != 0 else '0'
    return s
