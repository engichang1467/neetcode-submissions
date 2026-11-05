class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        h, res = {}, []
        for i in range(len(strs)):
            front_str = ''.join(sorted(strs[i]))
            if front_str not in h:    
                h[front_str] = [strs[i]]
            else:
                h[front_str].append(strs[i])

        for key, value in h.items():
            res.append(value)

        return res