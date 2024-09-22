class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        
        if len(nums) == 1:
            return 0
        nums = [float("-inf")] + nums
        nums.append(float("-inf"))
        l, r = 1, len(nums) - 2

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid - 1] <= nums[mid] >= nums[mid + 1]:
                return mid - 1
            
            if nums[mid + 1] > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1



        