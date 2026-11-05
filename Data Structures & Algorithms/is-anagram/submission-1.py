class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for i in t:
            if i not in s:
                return False
            
        return True
        
