class Solution:
    def maxScore(self, s: str) -> int:

        
        res = float("-inf")
        num_of_zeroes = 0
        num_of_ones = 0

        for i in range(len(s) - 1):
            c = s[i]
            if c == "0":
                num_of_zeroes += 1
            else:
                num_of_ones += 1
            
            res = max(res, num_of_zeroes - num_of_ones)
        
        if s[-1] == "1":
            num_of_ones += 1
        
        
        return res + num_of_ones
            
        