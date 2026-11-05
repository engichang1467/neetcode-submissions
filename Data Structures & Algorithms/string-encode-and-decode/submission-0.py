class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            if i != len(strs) - 1:
                res += strs[i] + ":;"
            else:
                res += strs[i]

        return res

    def decode(self, s: str) -> List[str]:
        return s.split(":;")
