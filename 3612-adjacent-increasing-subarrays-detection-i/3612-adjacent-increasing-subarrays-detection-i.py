class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums) - 2 * k + 1):
            if self.isIncreasing(nums[i:i + k]) and self.isIncreasing(nums[i + k: i + 2*k]):
                return True
        
        return False


    def isIncreasing(self, l):
        for i in range(1, len(l)):
            if l[i] <= l[i - 1]:
                return False
        return True