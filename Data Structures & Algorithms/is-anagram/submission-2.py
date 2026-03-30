class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        dict_s = dict.fromkeys(list_s,0)
        for elem in list_s:
            dict_s[elem] += 1
        
        list_t = list(t)
        dict_t = dict.fromkeys(list_t,0)
        for elem in list_t:
            dict_t[elem] += 1
        
        return dict_s == dict_t

        