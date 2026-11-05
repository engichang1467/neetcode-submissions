from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h, res = Counter(nums), []

        top_k = h.most_common(k)

        for k in top_k:
            res.append(k[0])

        return res