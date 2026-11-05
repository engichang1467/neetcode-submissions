class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}${word}"

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i].isdigit() and s[i+1] == "$":
                sub_str = ""
                str_len = int(s[i])
                i += 2
                for j in range(str_len):
                    sub_str += s[i]
                    i += 1
                
                res.append(sub_str)
        
        return res

