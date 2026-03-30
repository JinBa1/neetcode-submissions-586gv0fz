class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = list(strs[0])
        prefix = []
        for i, c in enumerate(first_str):
            for s in strs[1:]:
                if i > len(s) - 1: return "".join(prefix)
                if list(s)[i] != c: return "".join(prefix)
            prefix.append(c)
        return "".join(prefix)

