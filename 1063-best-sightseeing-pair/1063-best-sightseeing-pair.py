class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        max_seen = (values[0],0)
        res = 0


        for i in range(1, len(values)):
            num = values[i]
            res =  max(res, max_seen[0] + max_seen[1] + num - i)
            if num + i >= max_seen[0] + max_seen[1]:
                max_seen = (num, i)
        
        return res