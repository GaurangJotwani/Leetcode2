class Solution:
    def maximumLength(self, s: str) -> int:
        
        l = 0
        seen = defaultdict(int)
        counter = defaultdict(int)
        res = -1

        for r in range(len(s)):
            seen[s[r]] += 1

            while len(seen) > 1:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    seen.pop(s[l])
                l += 1
            
            for cnt in range(max(res,1),seen[s[r]] + 1):
                key = (s[r], cnt) 
                counter[key] += 1
                if counter[key] >= 3:
                    res = max(res, cnt)
        
        return res