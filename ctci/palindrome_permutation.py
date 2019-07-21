def palindrome_permutation(s):
    count = {}
    for c in s: count[c] = count[c] + 1 if c in count else 1
    odd = False
    for k in count:
        if count[k] % 2 == 1 and odd: return False
        elif count[k] % 2 == 1: odd = True
    return True

assert palindrome_permutation('aabb')
assert palindrome_permutation('abab')
assert palindrome_permutation('abcab')
assert not palindrome_permutation('abca')