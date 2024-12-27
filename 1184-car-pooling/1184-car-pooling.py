class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        buckets = [0] * 1001


        for trip in trips:

            cap, start, end = trip[0], trip[1], trip[2]

            buckets[start] += cap
            buckets[end] -= cap
        
        cap = 0
        for passengers in buckets:
            cap += passengers
            if cap > capacity:
                return False

        return True

            
            
            