class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:


        timestamps = []

        for start,end in intervals:
            timestamps.append((start, 1))
            timestamps.append((end, -1))
        
        timestamps.sort()
        c_cap = 0
        res = 0

        for timestamp, cap in timestamps:
            c_cap += cap
            res = max(res, c_cap)

        return res