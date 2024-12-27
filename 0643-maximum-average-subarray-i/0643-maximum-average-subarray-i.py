class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float("-inf")

        l = 0
        cSum = 0

        for r in range(len(nums)):

            cSum += nums[r]
            if r - l + 1 > k:
                cSum -= nums[l]
                l += 1
            
            if r - l + 1 == k:
                res = max(res, cSum / k)
        
        return res