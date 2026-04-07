class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starts = []
        for n in nums:
            if (n-1) not in nums_set:
                starts.append(n)
        
        max_length = 0
        for s in starts:
            base = s
            found = False
            while not found:
                base += 1
                if base not in nums_set:
                    found = True
            length = base - s
            max_length = length if length > max_length else max_length
        
        return max_length
