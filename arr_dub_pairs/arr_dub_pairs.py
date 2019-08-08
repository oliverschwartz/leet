def array_doubled_pairs(A):

    count = {}
    for n in A:
        count[n] = count[n] + 1 if n in count else 1

    while count != {}:
        val = next(iter(count))
        if val == 0 or ((val / 2) not in count and (val * 2) not in count):
            return False
        elif (val * 2) in count:
            count[val * 2] -= 1
            count[val] -= 1
        else:
            count[val / 2] -= 1
            count[val] -= 1
        for v in [val, val / 2, val * 2]:
            if v in count and count[v] == 0:
                del count[v]
    return True

assert(array_doubled_pairs([1, 2]))
assert(array_doubled_pairs([1, 2, 2, 4]))
assert(array_doubled_pairs([1, 2, 3, 6]))
assert(not array_doubled_pairs([1, 3]))
assert(not array_doubled_pairs([1, 2, 4, 4, 8, 16]))
assert(array_doubled_pairs([2, -2, -4, 4]))