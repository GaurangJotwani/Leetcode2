class Solution:

    def is1CharDiff(self,word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                continue
            diff += 1
            if diff > 1: return False
        return diff <= 1


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adjList = defaultdict(list)

        for i,word1 in enumerate(wordList):
            for j in range(i + 1, len(wordList)):
                word2 = wordList[j]
                if self.is1CharDiff(word1, word2):
                    adjList[word1].append(word2)
                    adjList[word2].append(word1)
        
        visited = set()
        q = deque()
        q.append((1,beginWord))
        visited.add(beginWord)

        while q:
            d,w1 = q.popleft()
            if w1 == endWord:
                return d
            
            for w2 in adjList[w1]:
                if w2 not in visited:
                    visited.add(w2)
                    q.append((d + 1, w2))
        
        
        return 0






        