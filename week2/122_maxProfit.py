class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = -prices[0]
        sell = 0
        for i in prices:
            buy = max(buy, sell - i)
            sell = max(sell, buy + i)
        return sell