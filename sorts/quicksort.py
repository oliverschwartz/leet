def quicksort(arr):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high + 1):
            if arr[j] <= pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        return i

    def helper(arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            helper(arr, low, p - 1)
            helper(arr, p + 1, high)

    return helper(arr, 0, len(arr) - 1)



import random
r1 = [x for x in range(20)]
random.shuffle(r1)
r2 = [x for x in range(20)]
random.shuffle(r2)
assert(sorted(r1) == quicksort(r2))