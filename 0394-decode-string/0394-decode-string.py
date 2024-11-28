class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i, char in enumerate(s):
            if char == "]":
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                rpt = ""
                while stack and stack[-1].isdigit():
                    rpt = stack.pop() + rpt
                rpt = int(rpt)
                tmp2 = ""
                for i in range(rpt):
                    tmp2 += temp
                stack.append(tmp2)
            else:
                stack.append(char)

        return "".join(stack)