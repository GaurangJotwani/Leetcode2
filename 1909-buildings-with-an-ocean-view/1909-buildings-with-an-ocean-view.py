class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        stk = []

        for i,h in enumerate(heights):

            while stk and h >= stk[-1][0]:
                stk.pop()
            
            stk.append((h,i))
        
        res = [idx for h,idx in stk]
        return res
