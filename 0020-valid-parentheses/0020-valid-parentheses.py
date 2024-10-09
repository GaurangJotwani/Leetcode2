class Solution:
    def isValid(self, s: str) -> bool:
        mp = { ")": "(", "]": "[", "}":"{"}
        stack = []
        for c in s:
            if c not in mp:
                stack.append(c)
                continue
            if not stack or stack[-1] != mp[c]:
                return False
            stack.pop()
        return not stack
