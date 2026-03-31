class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        major = nums[0]
        count = 0
        for n in nums:
            if n == major:
                count += 1
                if count > (0.5 * len(nums)) : break
            else:
                major = n
                count = 1
            
        
        return major