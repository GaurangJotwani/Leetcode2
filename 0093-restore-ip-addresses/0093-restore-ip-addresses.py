class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        if len(s) > 12 or len(s) < 4:
            return []
        res = []
        for i in range(1, 4):
            first = s[0:i]
            for j in range(1, 4):
                if i + j > len(s):
                    break
                second = s[i: i + j]
                for k in range(1, 4):
                    if i + j + k >= len(s):
                        break
                    third = s[i + j: i + j+ k]
                    fourth = s[i + j + k:]
                    if (self.isValidSubpart(first) and 
                        self.isValidSubpart(second) and
                        self.isValidSubpart(third) and
                        self.isValidSubpart(fourth)):
                        tmp = first + "." + second + "." + third + "." + fourth
                        res.append(tmp)
        return res

    def isValidSubpart(self, s):

        if len(s) == 1: 
            return True

        if len(s) > 3 or s[0] == "0" or not s.isdigit():
            return False
        if int(s) > 255: 
            return False
        return True
        