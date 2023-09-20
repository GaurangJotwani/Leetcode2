class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t): return False
        if not len(s): return True
        
        pt1, pt2 = 0, 0
        
        while pt2 < len(t):
            if s[pt1] == t[pt2]:
                pt1 += 1
                if pt1 == len(s): return True
            pt2 += 1
        
        
        return pt1 == len(s)
        