class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        for i,word1 in enumerate(words):
            for j in range(i + 1, len(words)):
                word2 = words[j]
                if not self.inOrder(word1, word2, order):
                    return False

        return True
    
    def inOrder(self, word1, word2, order):
        i, j = 0, 0
        print(word1, word2)
        while i < len(word1) and j < len(word2):
            w1 = order.index(word1[i])
            w2 = order.index(word2[i])
            print(w1)

            if w2 < w1:
                return False
            elif w1 < w2:
                return True

            i += 1
            j += 1
        
        if j == len(word2) and i < len(word1):
            return False
        
        return True

            