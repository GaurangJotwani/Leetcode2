class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        maxH = []

        for x,y in points:
            heappush(maxH, (-1 * (x**2 + y**2), x, y))

            if len(maxH) > k:
                heappop(maxH)
        
        res = [[x,y] for _,x,y in maxH]
        return res
            
        