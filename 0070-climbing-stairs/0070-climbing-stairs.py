class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: return 1
        if n == 2: return 2
        
        first, second = 1, 2
        for i in range(3, n + 1):
            temp = first + second
            first = second
            second = temp
        
        return second
        
         