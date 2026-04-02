class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        separator = 1
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            n = nums[mid]
            if n < separator:
                nums[mid] = nums[low]
                nums[low] = n
                low += 1
                mid += 1
            elif n > separator:
                nums[mid] = nums[high]
                nums[high] = n
                high -= 1
            else:
                mid += 1
