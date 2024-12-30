from sortedcontainers import SortedList


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        sl = SortedList()


        for num in nums:
            res += len(sl) - sl.bisect_right(num * 2)
            sl.add(num)
        
        return res