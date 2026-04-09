class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0 for _ in range(len(nums))]
        prefix_map = defaultdict(int)
        prefix_map[0] = 1
        res = 0
        for i in range(len(nums)):
            prefix[i] = prefix[i-1] + nums[i] if i != 0 else nums[i]
            
        
        for p in prefix:
            needed_prefix = p - k
            res += prefix_map[needed_prefix]
            prefix_map[p] += 1
        
        return res