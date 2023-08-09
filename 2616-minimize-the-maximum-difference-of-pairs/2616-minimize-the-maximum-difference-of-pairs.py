class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        if p == 0: return 0
        
        nums.sort()
        
        left = 0
        right = nums[-1] - nums[0]
        res = float("inf")
        
        while left <= right:
            
            mid = (left + right) // 2
            if self.helper(nums, p, mid):
                right = mid - 1
                res = min(res, mid)
            else:
                left = mid + 1
        
        return res
        
        
        
        
    
    
    def helper(self, nums, p, threshold):
        
        
        found = 0
        i = 0
        
        while i < len(nums) - 1:
            if abs(nums[i + 1] - nums[i]) <= threshold:
                found += 1
                if found == p: return True
                i += 2
            else:
                i += 1
        
        return False
        
        
        
        