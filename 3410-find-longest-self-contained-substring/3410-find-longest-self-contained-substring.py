class Solution:
    def maxSubstringLength(self, s: str) -> int:
        first = defaultdict(int)
        last = defaultdict(int)

        for i,ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        ans = -1
        n = len(s)
        print(first,last)
        for letter,i in first.items():
            mx_rng = last[letter]
            for j in range(i, n):
                a,b = first[s[j]], last[s[j]]
                if a < i:
                    break
                mx_rng = max(mx_rng, b)
                if mx_rng == j and j - i + 1 < n:
                    ans = max(ans, j - i + 1)
        
        return ans
                
