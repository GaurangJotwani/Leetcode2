class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        if len(nums) == 1:
            return 0

        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        res = float("inf")

        while l <= r:
            mid = l + (r - l) // 2
            if self.canFind(nums, mid, p):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return 0 if res == float("inf") else res
    
    def canFind(self, nums, val, p):
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= val:
                p -= 1
                if p == 0:
                    return True
                i += 2
            else:
                i += 1
        return False
        
        