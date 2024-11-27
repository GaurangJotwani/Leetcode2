class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        minH = []
        intervals.sort()
        ans = 0

        for interval in intervals:
            if minH and interval[0] >= minH[0][0]:
                heappop(minH)
                
            heappush(minH,(interval[1],interval[0]))
            ans = max(ans, len(minH))
        
        return ans

        
        