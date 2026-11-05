from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h, res = Counter(nums), []

        for key, value in h.items():
            if value >= k:
                res.append(key)

        return res