class Solution:
    def romanToInt(self, s: str) -> int:
        
        sm = 0
        i = 0
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        while i < len(s):
            char = s[i]
            if char == "I" and i + 1 < len(s):
                if s[i + 1] == "V":
                    sm += 4
                    i += 2
                    continue
                elif s[i + 1] == "X":
                    sm += 9
                    i += 2
                    continue
            elif char == "X" and i + 1 < len(s):
                if s[i + 1] == "L":
                    sm += 40
                    i += 2
                    continue
                elif s[i + 1] == "C":
                    sm += 90
                    i += 2
                    continue
            elif char == "C" and i + 1 < len(s):
                if s[i + 1] == "D":
                    sm += 400
                    i += 2
                    continue
                elif s[i + 1] == "M":
                    sm += 900
                    i += 2
                    continue
            sm += d[char]
            i += 1
        
        return sm