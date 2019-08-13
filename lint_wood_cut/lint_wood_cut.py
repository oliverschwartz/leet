# from https://www.lintcode.com/problem/wood-cut/description

def woodCut(L, k):
    # write your code here
    
    def is_valid(length):
        pieces = 0
        for l in L:
            pieces += l // length
        return pieces >= k
        
    max_length = 0
    l, r = 1, max(L)
    while l <= r:
        mid = (l + r) // 2
        if is_valid(mid):
            l = mid + 1
            max_length = mid
        else:
            r = mid - 1
            
    return max_length

assert woodCut([232, 124, 456], 7) == 114
assert woodCut([1, 2, 3], 7) == 0
assert woodCut([1, 2, 3], 6) == 1
assert woodCut([1, 115, 116], 2) == 115
assert woodCut([1, 115, 116], 1) == 116