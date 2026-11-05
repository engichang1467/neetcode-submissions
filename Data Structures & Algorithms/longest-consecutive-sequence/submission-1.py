class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set, seq_len = set(nums), 0

        for num in num_set:
            # check if the num is starting number
            if (num - 1) not in num_set:
                curr_len = 1
                # check if the next number of num is in the set
                while (num + curr_len) in num_set:
                    curr_len += 1
                
                seq_len = max(seq_len, curr_len)

        return seq_len

