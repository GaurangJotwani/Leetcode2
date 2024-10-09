class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        for i in range(26):
            c = chr(ord('a') + i)
            if abs(cnt2[c] - cnt1[c]) > 3:
                return False
        
        return True