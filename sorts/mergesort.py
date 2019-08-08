def mergesort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = n // 2
    left =  mergesort(arr[:mid])
    right =  mergesort(arr[mid:])

    i, j, k = 0, 0, 0
    while i < mid and j < n - mid:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < mid:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n - mid:
        arr[k] = right[j]
        j += 1
        k += 1
    return arr

import random
r1 = [x for x in range(20)]
random.shuffle(r1)
r2 = [x for x in range(20)]
random.shuffle(r2)
assert(sorted(r1) == mergesort(r2))