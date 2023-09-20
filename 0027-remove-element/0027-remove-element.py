class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            while left < right:
                if nums[right] != val:
                    break
                right -= 1
            

            if nums[left] != val:
                left += 1
                continue
            
            if left == right:
                return left
            
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        
        
        return left



        