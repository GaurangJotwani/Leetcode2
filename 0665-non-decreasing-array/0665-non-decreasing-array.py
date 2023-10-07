class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
        used = False
        
        for i in range(len(nums) - 1):
            
            if nums[i] <= nums[i + 1]:
                continue
            
            if used:
                return False
            
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i - 1]
                used = True
                continue
            
            used = True
            nums[i + 1] = nums[i]
        
        
        return True
            
        
        
        