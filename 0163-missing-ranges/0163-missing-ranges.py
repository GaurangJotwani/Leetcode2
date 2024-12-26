class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        
        number_needed = lower
        res = []

        for i,num in enumerate(nums):
            if num == number_needed:
                number_needed += 1
                continue
            if num < number_needed:
                continue
            res.append([number_needed, num - 1])
            number_needed = num + 1
        
        if number_needed <= upper:
            res.append([number_needed, upper])
        
        return res