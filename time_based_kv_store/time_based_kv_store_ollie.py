# Implementation: use a dictionary (a hash table)
# with keys as the `key` passed into the `set` method.
# The corresponding values are stored in a list (an array).
# Since the `set`s are called in increasing order of timestamp,
# we can append new tuples (of (value, timestamp)) to the array
# as they come. This way, when `get` is called, we can binary search
# the array as it is sorted.

# Runtime: 
# `set`: O(1)
# `get`: O(lgN)

class TimeMap:

    def __init__(self):
        self._map = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Check if the map contains the key
        if not self._map.__contains__(key):
            self._map[key] = [(value, timestamp)]
        else:
            self._map[key].insert(0, (value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self._map.__contains__(key): return ""
        
        arr = self._map[key]
        
        # check if the smallest value has time <= `timestamp`
        if arr[len(arr) - 1][1] > timestamp: return ""

        index = self._search(arr, 0, len(arr), timestamp)
        
        return arr[index][0]
        
    
    def _search(self, arr: list, lo, hi, target) -> int:
        if not lo < hi: 
            if hi < 0: return 0
            elif lo > len(arr) - 1: return len(arr) - 1
            else: return lo
        
        mid = (lo + hi) // 2   
        if arr[mid][1] == target: return mid
        elif arr[mid][1] > target: return self._search(arr, mid + 1, hi, target)
        else: return self._search(arr, lo, mid, target)
        