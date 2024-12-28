class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        prefix = [0] * len(nums)
        l,cSum = 0, 0
        for r in range(len(nums)):
            cSum += nums[r]
            if (r - l + 1) > k:
                cSum -= nums[l]
                l += 1
            
            if (r - l + 1) == k:
                prefix[l] = cSum
        
        cache = {}
        def dp(idx, remaining):
            if remaining <= 0 or idx >= len(prefix):
                return 0
            
            if (idx,remaining) in cache:
                return cache[(idx, remaining)]

            
            #Case 1: skip
            ans1 = dp(idx + 1, remaining)

            #Case: take it
            ans2 =  prefix[idx] + dp(idx + k, remaining - 1)
            cache[(idx, remaining)] = max(ans1, ans2)

            return max(ans1, ans2)
        
        indices = []
        def backtrack(idx, remaining):
            if idx >= len(prefix) or remaining == 0:
                return 0

            sum_with = prefix[idx] + dp(idx + k, remaining - 1)
            sum_without = dp(idx + 1, remaining)

            if sum_with >= sum_without:
                indices.append(idx)
                backtrack(idx + k, remaining - 1)
            else:
                backtrack(idx + 1, remaining)
        
        backtrack(0, 3)
        return indices


            

            





        