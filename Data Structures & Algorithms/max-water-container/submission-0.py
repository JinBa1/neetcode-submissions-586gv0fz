class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_water = 0
        while l < r:
            water = (r - l) * min(heights[r], heights[l])
            max_water = water if water > max_water else max_water
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            
        return max_water