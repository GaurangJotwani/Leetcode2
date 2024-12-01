class Solution:
    def intToRoman(self, num: int) -> str:
        lst = [("M",1000),("CM", 900),("D", 500),("CD", 400),("C", 100),("XC", 90),("L", 50),("XL", 40),("X", 10),("IX", 9),("V", 5),("IV", 4),("I", 1)]


        res = []


        for symb, val in lst:
            while num >= val:
                res.append(symb)
                num = num - val
                if num == 0:
                    break

        return "".join(res) 