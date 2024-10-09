class Solution:
    def digitCount(self, num: str) -> bool:
        freq = Counter(num)

        for i in range(len(num)):
            if freq[str(i)] != int(num[i]):
                return False

        return True
