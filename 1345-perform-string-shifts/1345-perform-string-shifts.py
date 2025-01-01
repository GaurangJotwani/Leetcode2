class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        total_shift = 0

        for dr, mag in shift:
            if dr == 0:
                total_shift -= mag
            else:
                total_shift += mag
        
        dr = 0 if total_shift < 0 else 1
        total_shift = abs(total_shift) % len(s)
        i = total_shift

        if dr == 0:
            s = s[i:] + s[:i]
        else:
            s = s[len(s) - i:] + s[:len(s) - i]
        
        return s

        