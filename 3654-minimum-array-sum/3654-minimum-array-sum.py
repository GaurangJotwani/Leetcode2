class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        
        dp = {}


        def helper(i, op1, op2):

            if i == len(nums):
                return 0

            if (i, op1, op2) in dp:
                return dp[(i, op1, op2)]
            
            #Case 1: do nothing
            ans = nums[i] + helper(i + 1, op1, op2)

            #Case 2: only op1
            if op1 > 0:
                ans = min(math.ceil(nums[i] / 2) + helper(i + 1, op1 - 1, op2), ans)
            
            #Case 3: only only op2
            if op2 > 0 and nums[i] >= k:
                ans = min(ans,nums[i] - k + helper(i + 1, op1, op2 - 1))
            
            if op1 > 0 and op2 > 0 and nums[i] >= k:
                # Case4: First subtract and then divide
                ans = min(ans, math.ceil((nums[i] - k)/2) + helper(i + 1, op1 - 1, op2 - 1))

                #Case5: First divide then subtract
                if math.ceil(nums[i] / 2) >= k:
                    ans = min(ans, math.ceil(nums[i] / 2) - k + helper(i + 1, op1 - 1, op2 - 1))
            
            dp[(i, op1, op2)] = ans
            return ans
        return helper(0, op1, op2)

