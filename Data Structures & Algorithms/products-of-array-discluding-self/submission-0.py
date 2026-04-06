class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_left = [1 for _ in range(len(nums)+1)]
        prod_right = [1 for _ in range(len(nums)+1)]

        padded_nums = [1 if (i == 0 or i == len(nums)+1) else nums[i-1] for i in range(len(nums)+2)]

        i = 1
        while i < len(nums)+1:
            prod_left[i] = prod_left[i-1] * padded_nums[i]
            i += 1
            
        i = len(nums)-1
        while i >= 0:
            prod_right[i] = prod_right[i+1] * padded_nums[i+2]
            i -= 1

        prod = [0 for _ in range(len(nums))]
        for ind in range(len(nums)):
            prod[ind] = prod_left[ind] * prod_right[ind]
        
        return prod
        
