class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # Define 32-bit mask and maximum value
        MAX = 0x7FFFFFFF  # Maximum positive 32-bit integer
        MASK = 0xFFFFFFFF  # Mask for 32 bits
        
        while num2 != 0:
            tmp = (num1 & num2) << 1  # Carry bits
            num1 = (num1 ^ num2) & MASK  # Sum without carry, masked to 32 bits
            num2 = tmp & MASK  # Carry bits, masked to 32 bits

        # Handle negative values (simulate 32-bit signed integer)
        return num1 if num1 <= MAX else ~(num1 ^ MASK)
