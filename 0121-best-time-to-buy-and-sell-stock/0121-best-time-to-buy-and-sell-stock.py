class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        buy_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if buy_price<prices[i]:
                profit = prices[i]-buy_price
                max_profit = max(max_profit,profit)
            else:
                buy_price = prices[i]
        return max_profit




        