class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        res = [-1] * len(nums)

        for i,num in enumerate(nums):
            idx = (i + k) % len(nums)
            res[idx] = num
        
        for i,num in enumerate(res):
            nums[i] = num
