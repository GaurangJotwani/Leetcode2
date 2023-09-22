class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, c_idx, right = 0, 0, len(nums) - 1

        while c_idx <= right:
            c_num = nums[c_idx]
            if c_num == 2:
                nums[c_idx], nums[right] = nums[right], nums[c_idx]
                right -= 1
            
            elif c_num == 0:
                nums[c_idx], nums[left] = nums[left], nums[c_idx]

                left += 1
                c_idx += 1
            else:
                c_idx += 1



