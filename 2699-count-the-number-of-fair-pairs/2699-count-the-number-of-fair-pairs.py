class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        cnts = 0
        for i in range(len(nums)):
            l_idx = self.left(nums, nums[i], lower, i + 1)
            if l_idx == -1:
                continue
            r_idx = self.right(nums, nums[i], upper, i + 1)
            if r_idx == -1:
                continue
            cnts += (r_idx - l_idx + 1)
        
        return cnts

    
    def left(self, nums, num, lower, l):
        r = len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if num + nums[mid] >= lower:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
    
    def right(self, nums, num, upper, l):
        r = len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if num + nums[mid] <= upper:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return res
