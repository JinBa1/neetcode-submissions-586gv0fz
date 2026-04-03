class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        freq_asc = {k : v for k, v in sorted(freq.items(), key = lambda item : item[1]) }
        return list(freq_asc.keys())[(-1 * k):]