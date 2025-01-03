class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        total = 0

        for c in s:
            if c == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
        
        return len(stack)