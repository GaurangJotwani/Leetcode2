class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        words = sentence.split()

        for i,word in enumerate(words):
            words[i] = self.convert(word, i + 1)


        return " ".join(words)
    
    def convert(self, word, idx):

        if word[0] in "aeiouAEIOU":
            word += "ma"
        else:
            word = word[1:] + word[0] + "ma"
        
        word += "a" * idx
        return word