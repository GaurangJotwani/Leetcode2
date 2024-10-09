# Approach
# Traverse the first half of the string; replace the first non-'a' character with 'a' to make it lexicographically smallest.
# If all characters are 'a', change the last character to 'b'.

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]

        return palindrome[:-1] + 'b'

# Time Complexity
# \U0001d442(\U0001d45b)
# O(n) where \U0001d45b
# n is the length of the string.