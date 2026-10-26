class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r;
            else:
                maxProfit = max(maxProfit, profit)

        return maxProfit

