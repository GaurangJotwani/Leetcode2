class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for word in strs:
            s = "".join(sorted(word))
            d[s].append(word)

        return list(d.values())