class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        output = []

        def helper(partial, o, c):

            if o == 0 and c == 0:
                output.append("".join(partial))
                return

            if o > 0:
                partial.append("(")
                helper(partial, o - 1, c)
                partial.pop()

            if c > o:
                partial.append(")")
                helper(partial, o, c - 1)
                partial.pop()
        
        
        helper([], n, n)
        return output

        