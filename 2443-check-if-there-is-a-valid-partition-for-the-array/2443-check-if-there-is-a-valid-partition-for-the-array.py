class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        dp = {}

        def dfs(i):

            if i == len(nums):
                return True
            
            if i in dp:
                return dp[i]
            
            ans = False
            # Case 1
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                ans = ans or dfs(i + 2)
            
            if i + 2 < len(nums) and nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
                ans = ans or dfs(i + 3)
            

            if i + 2 < len(nums) and nums[i + 1] - nums[i] == 1 and nums[i + 2] - nums[i + 1] == 1:
                ans = ans or dfs(i + 3)
            
            dp[i] = ans
            return dp[i]
        
        return dfs(0)
            


        