class Solution:
    def createDict(self, s: str) -> dict:
        result = {}
        for i in s:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1

        return result

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = self.createDict(s)
        t_dict = self.createDict(t)

        return s_dict == t_dict

        