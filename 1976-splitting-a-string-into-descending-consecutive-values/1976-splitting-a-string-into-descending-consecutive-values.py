class Solution:
    def splitString(self, s: str) -> bool:

       
        def helper(i, prev):

            for j in range(i, len(s)):
                cnum = int(s[i:j + 1])
                if prev - cnum == 1:
                    if (j + 1 == len(s)):
                        return True
                    if helper(j + 1, cnum):
                        return True
            
            return False



        
        for i in range(len(s) - 1):
            cnum = int(s[:i + 1])
            if helper(i + 1, cnum):
                return True
        
        
        return False



