class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left_sums = []
        c_sum = 0

        for num in nums:
            left_sums.append(c_sum)
            c_sum += num
        
        right_sums = [0] * len(nums)
        c_sum = 0

        for i in range(len(nums) - 1, -1, -1):
            right_sums[i] = c_sum
            c_sum += nums[i]
        
        for i in range(len(nums)):
            if left_sums[i] == right_sums[i]:
                return i
        
        return -1
        