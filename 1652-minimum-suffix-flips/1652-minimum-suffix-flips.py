class Solution:
    def minFlips(self, target: str) -> int:
        # Approach: Count transitions between consecutive characters in target 
        # from '0' to '1' or '1' to '0'; each transition requires a flip.
        # Time Complexity: 
        # \U0001d442(\U0001d45b) where n is the length of target.
        counts = 0
        last = '0'

        for t in target:
            if last != t:
                counts += 1
                last = t
        
        return counts