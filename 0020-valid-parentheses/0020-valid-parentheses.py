class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
                continue
            
            stack.append(char)
        return len(stack) == 0
    
    def test_1(self):
        assert(self.isValid("(((())))") == True)
        assert(self.isValid("(((()))))") == False)
        assert(self.isValid("()()}") == False)


        