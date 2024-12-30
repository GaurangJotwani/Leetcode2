class Solution:
    def maxSumAfterOperation(self, nums: list[int]) -> int:
        

        n = len(nums)

        left_sums = [0] * n
        right_sums = [0] * n

        cSum = 0

        for i,num in enumerate(nums):
            cSum += num
            left_sums[i] = max(cSum, 0)
            cSum = max(cSum, 0)
        
        
        cSum = 0
        for i in range(len(nums) -1, -1, -1):
            cSum += nums[i]
            right_sums[i] = max(0, cSum)
            cSum = max(0, cSum)
        
        res = 0
        for i,num in enumerate(nums):
            temp = num * num
            if i - 1 >= 0:
                temp += left_sums[i - 1]
            if i + 1 < len(nums):
                temp += right_sums[i + 1]
            res = max(res,temp)
        return res

        return 3