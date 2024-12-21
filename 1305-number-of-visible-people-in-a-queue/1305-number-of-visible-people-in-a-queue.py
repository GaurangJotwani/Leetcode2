class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []


        for i in range(len(heights) - 1, -1, -1):
            people_seen = 0
            cNum = heights[i]

            while stack and stack[-1] < cNum:
                people_seen += 1
                stack.pop()
            
            res[i] = people_seen
            if stack:
                res[i] += 1
            stack.append(cNum)
        
        return res