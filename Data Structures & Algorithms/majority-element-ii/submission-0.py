class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        uniques = set(nums)
        for num in uniques:
            count = 0
            for n in nums:
                count += 2 if n == num else -1
            if count > 0: res.append(num)
        return list(res)
