class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        patterns = defaultdict(list)
        for s in strings:
            pattern = ["0-"]
            for i in range(len(s) - 1):
                if ord(s[i + 1]) >= ord(s[i]):
                    pattern.append(str(ord(s[i + 1]) - ord(s[i])))
                else:
                    pattern.append(str(ord(s[i + 1]) + 26 - ord(s[i])))
                pattern.append("-")

            patterns["".join(pattern)].append(s)
        
        res = []
        for key,val in patterns.items():
            res.append(val)
        return res