class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        h = {}
        for i in range(len(strs)):
            front_str = ''.join(sorted(strs[i]))
            if front_str not in h:    
                h[front_str] = [strs[i]]
            else:
                h[front_str].append(strs[i])

        return list(h.values())