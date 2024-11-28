class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        inc_stack = []
        res = 0

        for i, height in enumerate(heights):
            idx = i
            while inc_stack and height < inc_stack[-1][1]:
                j,ht = inc_stack.pop()
                res = max(res,ht * (i - j))
                idx = j

            inc_stack.append((idx,height))
        
        while inc_stack:
            idx,ht = inc_stack.pop()
            res = max(res, ht * (len(heights) - idx))
        
        return res
        

