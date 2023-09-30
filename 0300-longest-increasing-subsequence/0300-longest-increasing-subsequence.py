class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(1,len(nums)):
            
            maxSub = float("-inf")
            for j in range(i):
                if nums[j] < nums[i]:
                    maxSub = max(maxSub, 1 + dp[j])
            
            dp[i] = max(dp[i], maxSub)
        
        return max(dp)



        