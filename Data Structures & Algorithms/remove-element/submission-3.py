class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)-1
        done = False

        nums.sort()

        while not done:
            if left > len(nums)-1 or right > len(nums)-1:
                done = True
            else:
                left_val = nums[left]
                right_val = nums[right]
                if val < left_val or val > right_val:
                        done = True
                elif left_val == val:
                    nums.pop(left)
                    right -= 1
                elif right_val == val:
                    nums.pop(right)
                    right -= 1
                else:
                    left += 1
                    right -= 1
                    
        
        return len(nums)
