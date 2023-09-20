from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        
        s_f = Counter(s)
        t_f = Counter(t)
        
        for key, val in s_f.items():
            if key not in t_f or val != t_f[key]:
                return False
        
        
        return True
        
        