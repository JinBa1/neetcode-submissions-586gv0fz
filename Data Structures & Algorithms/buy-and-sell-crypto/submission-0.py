class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_prof = 0
        for i in prices:
            if i < lowest:
                lowest = i
            else:
                prof = i - lowest
                max_prof = max(prof, max_prof)
        
        return max_prof