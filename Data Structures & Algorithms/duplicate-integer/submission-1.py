class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for num in nums:
            if num in h:
                return True
            else:
                h[num] = 1
        
        return False