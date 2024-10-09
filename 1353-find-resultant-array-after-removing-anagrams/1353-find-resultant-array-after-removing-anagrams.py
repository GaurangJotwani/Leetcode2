class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        output = []
        i = 0

        while i < len(words):
            word = words[i]
            j = i + 1
            while j < len(words) and sorted(word) == sorted(words[j]):
               j += 1
            output.append(word)
            i = j

        return output 
        