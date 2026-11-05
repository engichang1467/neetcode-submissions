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
                if len(stack) != 0 and check[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0


