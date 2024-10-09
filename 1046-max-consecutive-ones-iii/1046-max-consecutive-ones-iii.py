class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zero_count = max_length = 0
        for right in range(len(nums)):
            # Expand the window by including nums[right]
            if nums[right] == 0:
                zero_count += 1
            # If zero_count exceeds k, shrink the window from the left
            if zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            # Update the maximum length of the window
            max_length = max(max_length, right - left + 1)
        return max_length