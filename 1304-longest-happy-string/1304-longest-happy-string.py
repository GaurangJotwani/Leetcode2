class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))
        
        res = ""

        last_put = None
        while pq:
            freq, lett = heapq.heappop(pq)
            if (len(res) >= 2 and res[-1] == lett and res[-2] == lett):
                if not pq:
                    return res

                freq2, let2 = heapq.heappop(pq)
                heapq.heappush(pq,(freq, lett))
                res += let2
                freq2 += 1
                if freq2 != 0:
                    heapq.heappush(pq,(freq2, let2))
            else:
                res += lett
                freq += 1
                if freq != 0:
                    heapq.heappush(pq, (freq, lett))
        
        return res




            
            
            
        