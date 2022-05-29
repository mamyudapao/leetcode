class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      minimum = float('inf')
      max_profit = 0
      for i in range(len(prices)):
        if prices[i] < minimum:
          minimum = prices[i]
        if max_profit < prices[i] - minimum:
          max_profit = prices[i] - minimum
      return max_profit