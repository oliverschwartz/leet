# from ctci

def is_permutation(s1, s2):
    s1_count, s2_count = {}, {}
    for c in s1: s1_count[c] = s1_count[c] + 1 if c in s1_count else 1
    for c in s2: s2_count[c] = s2_count[c] + 1 if c in s2_count else 1 
    return s1_count == s2_count

assert is_permutation('abba', 'baba')
assert not is_permutation('aba', 'bab')
