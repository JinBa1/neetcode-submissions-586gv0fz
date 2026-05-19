class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup_check = set()
        res = 0
        l, r = 0, 0
        curr_max = r - l 
        while r < len(s):
            assert l <= r
            c = s[r]
            if c in dup_check:
                while l < r:
                    rc = s[l]  # remove candidate until previous instance of dup key is excluded in the new sub string
                    dup_check.remove(s[l])
                    l += 1
                    if rc == c: break
            
            dup_check.add(c)  # removal would remove the previous dup key, so add it back when checking new
            r += 1
            curr_max = max(r - l, curr_max)  # only store the maximum len found
        
        return curr_max