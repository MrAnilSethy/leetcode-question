class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float("inf")
        max_profit = 0

        for price in prices:
            buy_price = min(buy_price, price)
            profit = price - buy_price
            max_profit = max(max_profit, profit)

        return max_profit