class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n <= 0:
            return False

        i, set_bits = 0, 0
        while (n > 0):
            if n & 1:
                set_bits += 1
                if set_bits > 1 or i % 2:
                    return False
            i += 1
            n = n >> 1
        
        return True
                


        