class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        

        minH = []
        trips.sort(key = lambda trip: trip[1])
        c_cap = 0

        for trip in trips:
            
            cap, start, end = trip

            while minH and start >= minH[0][0]:
                _,_, c = heappop(minH)
                c_cap -= c

            heappush(minH, (end,start,cap))
            
            c_cap += cap
            if c_cap > capacity:
                return False
        
        return True
