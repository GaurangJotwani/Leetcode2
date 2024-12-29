class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 5001
        for num in nums:
            buckets[num] += 1
        
        right = 5000
        idx = 1
        while idx < len(nums):
            
            while right >= 0 and buckets[right] == 0:
                right -= 1
            nums[idx] = right
            buckets[right] -= 1
            idx += 2
        
        idx = 0
        while idx < len(nums):
            
            while right >= 0 and buckets[right] == 0:
                right -= 1
            nums[idx] = right
            buckets[right] -= 1
            idx += 2
        
        return nums

                


        