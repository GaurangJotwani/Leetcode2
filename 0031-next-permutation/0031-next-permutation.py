class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the rightmost pair where nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # Step 2: Find the smallest number larger than nums[i] in nums[i+1:]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # Swap nums[i] with nums[j]

        # Step 3: Reverse the subarray nums[i+1:]
        nums[i + 1:] = reversed(nums[i + 1:])
        