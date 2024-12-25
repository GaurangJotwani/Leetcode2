class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        p1 = 0
        p2 = 0

        while p1 < len(word) and p2 < len(abbr):
            if abbr[p2] == "0":
                return False
            num = ""
            while p2 < len(abbr) and abbr[p2].isnumeric():
                num += abbr[p2]
                p2 += 1
            if not num:
                if word[p1] != abbr[p2]:
                    return False
                if p1 == len(word) - 1 and p2 == len(abbr) - 1:
                    return True
                p1 += 1
                p2 += 1
            else:
                num = int(num)
                p1 += num
            if p1 == len(word) and p2 == len(abbr):
                    return True
        
        return False