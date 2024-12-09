class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        i, j = 0, 0

        for i,char in enumerate(str1):
            if j == len(str2):
                return True
            if char == str2[j]:
                j += 1
            
            elif char == "z" and str2[j] == "a":
                j += 1
            
            elif ord(char) == ord(str2[j]) - 1:
                j += 1
            
        
        return j == len(str2)
        