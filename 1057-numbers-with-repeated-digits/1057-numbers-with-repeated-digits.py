from math import factorial

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        return n - self.countNumbersWithUniqueDigits(n)

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # Convert n to its digit array
        digits = list(map(int, str(n)))
        length = len(digits)
        unique_count = 0
        
        # Count numbers with unique digits for lengths less than `length`
        for i in range(1, length):
            unique_count += 9 * self.perm(9, i - 1)  # Leading digit has 9 choices, remaining (i - 1) positions have decreasing choices

        # Track digits used in the current number
        seen = set()
        
        # Count numbers with unique digits for the current length
        for i in range(length):
            for x in range(1 if i == 0 else 0, digits[i]):
                if x not in seen:
                    unique_count += self.perm(9 - i, length - i - 1)
            if digits[i] in seen:
                break
            seen.add(digits[i])
        
        # Add 1 if the number itself has all unique digits
        if len(seen) == length:
            unique_count += 1
            
        return unique_count

    def perm(self, a: int, b: int) -> int:
        # Returns the number of permutations P(a, b) = a * (a - 1) * ... * (a - b + 1)
        result = 1
        for i in range(b):
            result *= a - i
        return result
