class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # 1,4,16,64
        # 1, 100, 10000, 1000000
        # 2**2a --> (2**2)**a --> 4**a

        if n <= 0:
            return False
        
        set_bits, i = 0, 0
        while n > 0:
            if n & 1:
                set_bits += 1
                if set_bits > 1 or i % 2:
                    return False
            i += 1
            n = n // 2
        
        return True