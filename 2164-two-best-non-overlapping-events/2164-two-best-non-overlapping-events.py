class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        non_overlapping = []
        overlapping = []
        res = float("-inf")

        for s,e,v in events:
            while overlapping and s > overlapping[0][0]:
                e1,s1,v1 = heappop(overlapping)
                heappush(non_overlapping,(-v1,s1,e1))
            
            res = max(res, v)
            if non_overlapping:
                res = max(res, v + -1 * non_overlapping[0][0])
            heappush(overlapping, (e,s,v))

        return res