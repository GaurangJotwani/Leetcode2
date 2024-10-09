class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1  # Only "0" for n = 0
    
        unique_count = 10  # Start with n=1 case (0 to 9)
        available_digits = 9  # Choices for the first digit (1-9 for n > 1)
        current_unique = 9  # Unique-digit count for current length
        
        for i in range(2, n + 1):
            current_unique *= available_digits  # Choose unique digit for each position
            unique_count += current_unique  # Add to the total count
            available_digits -= 1  # Decrement choices for each successive position
        
        return unique_count