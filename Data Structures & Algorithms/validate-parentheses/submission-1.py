class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(':')', '{':'}', '[':']'}
        stack = []

        for i in range(len(s)):
            # if its open bracket
            if s[i] in check:
                stack.append(s[i])
            # if its close bracket
            else:
                temp = stack.pop()
                if check[temp] == s[i]:
                    continue
                else:
                    return False
        
        return True


