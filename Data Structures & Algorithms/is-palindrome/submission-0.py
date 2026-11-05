class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        cleaned = ''.join(char for char in s if char.isalnum())
        reversed = cleaned[::-1]

        return cleaned == reversed
