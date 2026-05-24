class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        window = defaultdict(int)
        max_freq = 0

        for r in range(len(s)):
            window[s[r]] += 1
            max_freq = max(max_freq, window[s[r]])

            # (window size) - (count of most frequent char) = chars we'd need to replace
            while (r - l + 1) - max_freq > k:
                window[s[l]] -= 1   # decrement the leaving char FIRST
                l += 1              # then move left pointer

            res = max(res, r - l + 1)

        return res