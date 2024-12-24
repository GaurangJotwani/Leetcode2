class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [-1] * n
        nums = nums + nums
        stack = []

        for i,num in enumerate(nums):

            while stack and stack[-1][0] < num:
                
                res[stack[-1][1] % n] = num
                stack.pop()
            stack.append((num,i))

        return res
        