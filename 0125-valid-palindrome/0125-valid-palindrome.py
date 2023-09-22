class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = []
        for char in s:
            # print(char)
            if ord("a") <= ord(char) <= ord("z") or ord("A") <= ord(char) <= ord("Z"):
                newStr.append(char.lower())
            elif char in "0123456789":
                newStr.append(char)
        
        print(newStr)
        left, right = 0, len(newStr) - 1
        while left < right:
            if newStr[left] != newStr[right]:
                return False
            left += 1
            right -= 1
        
        return True

