class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left, right = 0, len(nums) - 1
        
        
        while left <= right:
            
            
            mid = (left + right) // 2
            
            
            cNum = nums[mid]
            
            if cNum == target:
                return True
            
            if cNum == nums[left] and cNum == nums[right]:
                left += 1
                right -=1
                continue
            
            
            # it is sorted...
            if nums[left] < nums[right]:
                
                if cNum < target:
                    left = mid + 1
                else:
                    right = mid - 1
                continue
            
            #left side is sorted
            if nums[left] <= cNum:
                
                if target < cNum and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                
                if target <= nums[right] and target > cNum:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
            
            
            
        
        return False
                
        
        
        
        
        
        
        