class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        max_seen = float("-inf")
        res = []

        for i in range(len(heights) - 1, -1, -1):
            c_h = heights[i]
            if c_h > max_seen:
                res.append(i)
                max_seen = c_h
        
        res.reverse()
        return res

