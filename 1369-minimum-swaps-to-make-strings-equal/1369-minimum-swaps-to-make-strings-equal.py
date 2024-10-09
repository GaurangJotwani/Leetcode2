class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy_count, yx_count = 0, 0
    
        # Count the mismatches
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy_count += 1
            elif a == 'y' and b == 'x':
                yx_count += 1
        
        # If the total number of mismatches is odd, return -1
        if (xy_count + yx_count) % 2 != 0:
            return -1
        
        # Calculate the minimum swaps
        swaps = (xy_count // 2) + (yx_count // 2)
        
        # If there is an unpaired mismatch (both counts are odd), add 2 swaps
        if xy_count % 2 == 1:
            swaps += 2
        
        return swaps
        