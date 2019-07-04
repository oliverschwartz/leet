class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        n = len(prices)
        if n == 0: return profit
        
        buy_price = prices[0]
        for i in range(1, n):
            
            if prices[i] < prices[i - 1] and prices[i - 1] > buy_price:
                profit += prices[i - 1] - buy_price
                buy_price = prices[i]
                
            elif prices[i] < prices[i - 1]:
                buy_price = prices[i]
                
            # must sell at the end of the period
            if i == n - 1 and prices[i] > buy_price:
                profit += prices[i] - buy_price
                
        return profit