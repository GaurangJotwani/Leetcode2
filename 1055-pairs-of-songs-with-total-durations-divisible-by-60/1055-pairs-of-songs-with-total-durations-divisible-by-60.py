# Approach
# Use a hashmap to count occurrences of each remainder when divided by 60.
# For each song, check for pairs that add up to 60 with the complement remainder.
# Time Complexity
# \U0001d442(\U0001d45b) where \U0001d45b
# n is the length of the time list.

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_count = [0] * 60
        count = 0

        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60  # handles cases where remainder is 0
            count += remainder_count[complement]  # add pairs
            remainder_count[remainder] += 1      # update remainder count

        return count