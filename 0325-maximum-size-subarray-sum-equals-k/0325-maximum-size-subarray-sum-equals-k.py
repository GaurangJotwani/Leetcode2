class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {}
        cSum = 0
        prefix_arr = [0]
        for num in nums:
            cSum += num
            prefix_arr.append(cSum)
        
        res = 0
        print(prefix_arr)
        for i,sm in enumerate(prefix_arr):
            diff = sm - k
            if diff in d:
                res = max(res, i - d[diff])
            if sm not in d:
                d[sm] = i
        

        return res