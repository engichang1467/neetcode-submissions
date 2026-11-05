import math as m

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):

            if i == 0:
                prod = m.prod(nums[i+1:len(nums)])
            elif i == len(nums)-1:
                prod = m.prod(nums[0:len(nums)-1])
            else:
                prod = m.prod(nums[0:i]) * m.prod(nums[i+1:len(nums)])
            res.append(prod)
        
        return res