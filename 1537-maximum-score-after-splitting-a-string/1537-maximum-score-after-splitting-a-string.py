class Solution:
    def maxScore(self, s: str) -> int:

        total_ones = 0
        for c in s:
            if c == "1":
                total_ones += 1
        res = 0
        
        num_of_zeroes = 0
        num_of_ones = 0

        for i in range(len(s) - 1):
            c = s[i]
            if c == "0":
                num_of_zeroes += 1
            else:
                num_of_ones += 1
            print(num_of_ones)
            print(num_of_zeroes)
            print("------")
            res = max(res, total_ones - num_of_ones + num_of_zeroes)
        
        return res
            
        