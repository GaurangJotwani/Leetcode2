class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        if len(nums) == 1:
            return True
        finishLine = len(nums) - 1
        i = finishLine

        while i >= 0:
            if i + nums[i] >= finishLine:
                finishLine = i
            i -= 1
        
        return finishLine == 0


        