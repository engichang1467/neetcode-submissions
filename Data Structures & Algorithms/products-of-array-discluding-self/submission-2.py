import math as m

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, res = len(nums), []
        prefix = [0 for i in range(n)]
        suffix = [0 for i in range(n)]

        prefix[0] = suffix[n-1] = 1

        # create prefix
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        # create suffix
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        # mutiply them both together
        for i in range(n):
            res.append(prefix[i] * suffix[i])

        return res