class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 1
        result = 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            if prices[r] > prices[l]:
                result = max(profit, result)
            else:
                l = r

            r += 1
        
        return result
    

    
              