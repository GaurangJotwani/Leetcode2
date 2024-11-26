class Solution:
    def trap(self, height: List[int]) -> int:

        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        
        maxL = 0
        for i,h in enumerate(height):
            leftMax[i] = maxL
            maxL = max(maxL, h)
        
        maxR = 0
        for r in range(len(height) - 1, -1, -1):
            rightMax[r] = maxR
            maxR = max(maxR, height[r])
        
        ans = 0
        for i in range(len(height)):
            temp = min(leftMax[i], rightMax[i]) - height[i]
            if temp > 0:
                ans += temp
        
        return ans
