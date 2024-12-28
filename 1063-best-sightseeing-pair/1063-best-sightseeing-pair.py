class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        test = values[0]
        res = 0


        for i in range(1, len(values)):
            num = values[i]
            res =  max(res, test + num - i)
            if num + i >= test:
                test = num + i
        
        return res