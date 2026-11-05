class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set, seq_len = set(nums), 0

        for num in nums:
            curr_len = 0
            while (num + curr_len in num_set):
                curr_len += 1
            
            seq_len = max(seq_len, curr_len)

        return seq_len

