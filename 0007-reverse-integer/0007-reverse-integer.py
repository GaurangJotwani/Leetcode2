class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        curr = 0

        while x:
            curr = curr * 10 + x % 10
            x = x // 10
        
        if curr >= (2**31 - 1):
            return 0
        return -curr if sign == -1 else curr