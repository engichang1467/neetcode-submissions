class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        curr = []
        for i in range(len(nums)):
            curr.append([nums[i], i])

        i, j = 0, len(nums) - 1
        while i < j:

            temp_res = curr[i][0] + curr[j][0]

            if temp_res == target:
                return [curr[i][1], curr[j][1]]

            elif temp_res > target:
                j -= 1
            else:
                i += 1

        return
