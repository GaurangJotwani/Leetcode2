class Solution:
    def minFlips(self, target: str) -> int:
        # Count transitions; initial count starts with 0 if first char is '0' else 1
        flips = int(target[0] == '1') + sum(target[i] != target[i - 1] for i in range(1, len(target)))
        return flips