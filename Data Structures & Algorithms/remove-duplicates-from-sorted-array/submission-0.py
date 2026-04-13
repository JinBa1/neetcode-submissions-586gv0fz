class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w_ptr = 0
        for n in nums:
            if n != nums[w_ptr]:
                w_ptr += 1
                nums[w_ptr] = n
        
        return w_ptr+1