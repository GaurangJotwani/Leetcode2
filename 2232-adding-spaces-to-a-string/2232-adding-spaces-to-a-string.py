class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        p1 = 0
        p2 = 0
        res = []

        while p1 < len(s):
            
            if p2 == len(spaces) or p1 < spaces[p2]:
                res.append(s[p1])
                p1 += 1
                continue
            res.append(" ")
            p2 += 1
        
        return "".join(res)

        