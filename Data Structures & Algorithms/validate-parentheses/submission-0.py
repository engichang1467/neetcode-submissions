class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(':')', '{':'}', '[':']'}
        stack =[s[0]]

        for i in range(1, len(s)):
            temp = stack.pop()
            # if its open bracket
            if s[i] in check:
                stack.append(temp)
                stack.append(s[i])
            # if its close bracket
            else:
                if check[temp] == s[i]:
                    continue
                else:
                    return False
        
        return True


