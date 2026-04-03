class Solution:

    def encode(self, strs: List[str]) -> str:
        builder = []
        for s in strs:
            builder.append(str(len(s)))
            builder.append("#")
            builder.append(s)
        
        return "".join(builder)

    def decode(self, s: str) -> List[str]:
        n_strs = []
        i = 0
        num_len = 0
        while i < len(s):
            c = s[i]
            if c == "#":
                next_len = int(s[i-num_len : i])
                n_strs.append(s[i+1 : i+next_len+1])
                num_len = 0
                i += next_len + 1
            else:
                i += 1
                num_len += 1
        return n_strs