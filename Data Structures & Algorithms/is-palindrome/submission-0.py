class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = s.casefold()
        l, r = 0, len(ss)-1
        while l < r:
            if not ss[l].isalnum():
                l += 1
                continue
            if not ss[r].isalnum():
                r -= 1 
                continue
            if ss[l] != ss[r]:
                return False
            l += 1
            r -= 1
        return True