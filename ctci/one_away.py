# from ctci

def one_away(s, t):
    n, m = len(s), len(t)
    if n - m > 1 or n - m < -1: return False
    i, j = 0, 0
    replaced, inserted = False, False
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
            j += 1
        elif n == m and not replaced:
            i += 1
            j += 1
            replaced = True
        elif n != m and not inserted:
            if n > m: i += 1
            elif m > n: j += 1
            inserted = True
        else: return False
    return True

assert one_away('pale', 'ple')
assert one_away('pales', 'pale')
assert one_away('pale', 'bale')
assert not one_away('pale', 'bake')