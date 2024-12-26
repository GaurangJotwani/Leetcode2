class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                continue
            if nums[i] - nums[i - 1] - 1 >= k:
                return nums[i - 1] + k
            else:
                k -= nums[i] - nums[i - 1] - 1
        
        if k > 0:
            return nums[-1] + k
        



        