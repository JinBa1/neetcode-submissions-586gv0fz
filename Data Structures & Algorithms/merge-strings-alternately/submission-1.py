class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res_len = min(len(word1), len(word2)) * 2 + max(len(word1), len(word2)) - min(len(word1), len(word2))
        res = ['' for _ in range(res_len)]
        i, w = 0, 0
        while i < min(len(word1), len(word2)) * 2 - 1:
            res[i], res[i+1] = word1[w], word2[w]
            i += 2
            w += 1
        
        res[i : ] = word1[w : ] if w < len(word1)-1 else word2[w : ]
        return "".join(res)
            