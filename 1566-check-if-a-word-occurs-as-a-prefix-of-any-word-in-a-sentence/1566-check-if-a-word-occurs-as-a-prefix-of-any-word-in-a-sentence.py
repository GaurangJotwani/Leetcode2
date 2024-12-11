class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = sentence.split()
        res = -1

        for i,word in enumerate(sentence):
            if word.startswith(searchWord):
                res = i + 1
                break
        
        return res