class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:

        cache = {}
        res = [0]
        def dfs(idx, used):

            if idx == len(nums):
                return 0

            if (idx, used) in cache: 
                return cache[(idx, used)]

            ans1 = nums[idx] + dfs(idx + 1, used)


            if not used:
                ans1 = max(ans1, nums[idx] * nums[idx] + dfs(idx + 1, not used))

            
            res[0] = max(res[0], ans1)
            cache[(idx, used)] = max(0 ,ans1)
            return cache[(idx, used)]
        
        dfs(0, False)
        return res[0]
            




        