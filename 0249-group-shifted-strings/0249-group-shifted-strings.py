class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        patterns = defaultdict(list)
        for s in strings:
            pattern = ""
            if len(s) == 1:
                patterns["0"].append(s)
                continue
            
            for i in range(len(s) - 1):
                if ord(s[i + 1]) >= ord(s[i]):
                    pattern += str(ord(s[i + 1]) - ord(s[i])) + "-"
                else:
                    pattern += str(ord(s[i + 1]) + 26 - ord(s[i])) + "-"

            patterns[pattern].append(s)
        
        res = []
        for key,val in patterns.items():
            res.append(val)
        return res