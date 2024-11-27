class Solution:
    def calculate(self, s: str) -> int:
        res = prev = 0
        cur_operation = "+"

        i = 0

        while i < len(s):

            curr_char = s[i]
            if curr_char.isdigit():
                cur = 0
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1
                if cur_operation == "+":
                    res += cur
                    prev = cur
                elif cur_operation == "-":
                    res -= cur
                    prev = -cur
                elif cur_operation == "*":
                    res -= prev
                    res += prev * cur
                    prev = prev * cur
                else:
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)
            elif curr_char != " ":
                cur_operation = s[i]
            i += 1
        
        return res

