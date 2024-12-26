class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        

        unique = len(set(s))
        res = 0

        for uni_cnt in range(1, unique + 1):

            counter = defaultdict(int)
            l = 0

            for r in range(len(s)):

                counter[s[r]] += 1

                while len(counter) > uni_cnt:
                    counter[s[l]] -= 1
                    if counter[s[l]] == 0:
                        counter.pop(s[l])
                    l += 1
                
                if self.isValid(counter, k):
                    res = max(res, r - l + 1)
                
        
        return res
    
    def isValid(self, counter, k):
        for key,val in counter.items():
            if val < k:
                return False
        return True


