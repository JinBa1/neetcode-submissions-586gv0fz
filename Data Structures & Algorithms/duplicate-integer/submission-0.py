class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set([])
        hashset.update(nums)

        return len(hashset) < len(nums)