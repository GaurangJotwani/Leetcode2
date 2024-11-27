class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        result = [intervals[0]]
        curr = result[0]
        
        for interval in intervals[1:]:
            if interval[0] <= curr[1]:
                curr[1] = max(curr[1], interval[1])
            else:
                result.append(interval)
                curr = result[-1]

        return result