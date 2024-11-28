class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float("-inf")
        cSum = 0

        for num in nums:
            cSum = max(cSum + num, num)
            max_sum = max(max_sum, cSum)
        
        return max_sum