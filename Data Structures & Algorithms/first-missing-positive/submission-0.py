class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 1
        for i in range(len(unique)):
            if res not in unique:
                break
            res += 1
        return res