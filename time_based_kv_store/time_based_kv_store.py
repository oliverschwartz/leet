class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.vals: self.vals[key].append((timestamp, value))
        else: self.vals[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals: return ''

        def binarySearch(arr):
            output = ''
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] > timestamp:
                    right = mid - 1
                else:
                    output = arr[mid][1]
                    left = mid + 1
            return output
            
        return binarySearch(self.vals[key])