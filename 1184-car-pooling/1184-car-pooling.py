class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        buckets = [0] * 1001


        for trip in trips:

            cap, start, end = trip[0], trip[1], trip[2]

            for i in range(start + 1, end + 1):
                buckets[i] += cap
                if buckets[i] > capacity:
                    return False
        

        return True

            
            
            