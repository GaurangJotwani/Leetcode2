class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        seen = {}
        for num in nums:
            seen[num] = False
        

        longest = 0

        for idx, num in enumerate(nums):

            if seen[num]:
                continue
            left, right = num - 1, num + 1
            while right in seen:
                seen[right] = True
                right += 1
            
            while left in seen:
                seen[left] = True
                left -= 1
            
            longest = max(longest, right - left - 1)
        
        return longest
        