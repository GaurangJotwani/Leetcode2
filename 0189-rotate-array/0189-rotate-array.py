class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)

        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, 0, len(nums) - 1)


    
    def reverse(self, nums, l ,r):
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1
        
        
