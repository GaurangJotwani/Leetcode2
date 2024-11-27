class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        finishLine = len(nums) - 1
        i = finishLine - 1

        while i >= 0:
            if i + nums[i] >= finishLine:
                finishLine = i
            i -= 1
        
        return finishLine == 0


        