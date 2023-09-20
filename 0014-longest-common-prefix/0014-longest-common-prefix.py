class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = ""
        smallest = ""
        n = float("inf")
        for word in strs:
            if len(word) < n:
                smallest = word
                n = len(word)
        left, right = 0, len(smallest) - 1
        while left <= right:
            mid = (left + right) // 2
            c_pot = smallest[:mid + 1]
            if self.isCommon(c_pot, strs):
                ans = c_pot
                left = mid + 1
            else:
                right = mid - 1
        return ans
    
    def isCommon(self, pot, strs):
        n = len(pot)
        for word in strs:
            if word[:n] != pot:
                return False
        return True
        