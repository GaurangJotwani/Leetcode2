class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        minH = []
        total_n = len(nums)
        n = total_n // 3
        sm = 0
        maximums = [0] * len(nums)

        for i in range(len(nums) - 1, n - 1, -1):
            sm += nums[i]
            heappush(minH, nums[i])
            if len(minH) < n:
                continue
            if len(minH) > n:
                sm -= heappop(minH)
            maximums[i] = sm
        
        res = float("inf")
        sm = 0
        maxH = []
        for i in range(0,2 * n):
            sm += nums[i]
            heappush(maxH, -1 * nums[i])
            if len(maxH) < n:
                continue
            if len(maxH) > n:
                sm -= -1 * heappop(maxH)
            # print(i, maxH, maximums, sm)
            res = min(res, sm - maximums[i + 1])
        
        return res

