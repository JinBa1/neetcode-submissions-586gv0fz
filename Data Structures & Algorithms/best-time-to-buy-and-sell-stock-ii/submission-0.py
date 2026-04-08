class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for day in range(len(prices)-1):
            price_today, price_tomorrow = prices[day], prices[day+1]
            max_profit += max((price_tomorrow - price_today), 0)
        return max_profit