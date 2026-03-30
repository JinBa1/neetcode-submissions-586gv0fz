class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_maps = {}
        for str in strs:
            alphabets = [0 for i in range(26)]
            for c in list(str):
                alphabets[ord(c)-97] += 1
            t_alphabets = tuple(alphabets)
            if t_alphabets in strs_maps:
                strs_maps[t_alphabets].append(str)
            else:
                strs_maps[t_alphabets] = [str]
        return list(strs_maps.values())

