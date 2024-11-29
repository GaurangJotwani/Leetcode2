class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l_idx = self.leftMost(nums, target)
        r_idx = self.rightMost(nums, target)
        return [l_idx, r_idx]
    
    def rightMost(self, nums, target):
        l,r,res = 0,len(nums) - 1,-1
        while l <= r:
            mid = (l + r) // 2
            cNum = nums[mid]
            if cNum < target:
                l = mid + 1
            elif cNum > target:
                r = mid - 1
            else:
                res = mid
                l = mid + 1

        return res
    def leftMost(self, nums, target):
        l = 0
        r = len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            cNum = nums[mid]

            if cNum < target:
                l = mid + 1
            elif cNum > target:
                r = mid - 1
            else:
                res = mid
                r = mid - 1

        return res
        