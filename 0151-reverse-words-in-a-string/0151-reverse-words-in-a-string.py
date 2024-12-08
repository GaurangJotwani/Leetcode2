class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split(" ")
        s.reverse()
        new_ls = []
        for word in s:
            if word != "":
                new_ls.append(word)
        return " ".join(new_ls)
        