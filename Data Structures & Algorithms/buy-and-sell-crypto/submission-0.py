class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        maxProfit = 0
        for i in range(1, len(prices)):
            print(prices[i] - prices[buyDay])
            if prices[i] > prices[buyDay]:
                maxProfit = max(prices[i] - prices[buyDay], maxProfit)
            else:
                buyDay = i
        return maxProfit