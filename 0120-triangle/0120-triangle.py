class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        rows = len(triangle)
        
        for r in range(1,rows):
            for i in range(r + 1):
                left = triangle[r - 1][i - 1] if i - 1 >= 0 else float("inf")
                up = triangle[r - 1][i] if i < r else float("inf")
                triangle[r][i] += min(left, up)
            
        

        return min(triangle[-1])

        