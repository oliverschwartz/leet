class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.memo = {}
        coins.sort()
        
        def numWays(amount, prev, coin_subset):
            if amount == 0:
                return 1
            else:
                if (amount, prev) not in self.memo:
                    ways = 0
                    for index, c in enumerate(coin_subset):
                        if c <= prev and amount - c >= 0:
                            ways += numWays(amount - c, c, coin_subset[:index + 1])
                    self.memo[(amount, prev)] = ways
            
            return self.memo[(amount, prev)]
        
        return numWays(amount, 5000, coins)
        
