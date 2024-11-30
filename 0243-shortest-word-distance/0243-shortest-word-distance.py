class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        indices1 = []
        indices2 = []

        for i,word in enumerate(wordsDict):
            if word == word1:
                indices1.append(i)
            elif word == word2:
                indices2.append(i)
        
        p1,p2 = 0, 0
        res = float("inf")

        while p1 < len(indices1) and p2 < len(indices2):
            if indices1[p1] < indices2[p2]:
                res = min(indices2[p2] - indices1[p1], res)
                p1 += 1
            else:
                res = min(indices1[p1] - indices2[p2], res)
                p2 += 1
        
        return res
        