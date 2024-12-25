class Solution:
    def customSortString(self, order: str, s: str) -> str:

        def customCmp(c):
            if order.find(c) == -1:
                return 27
            else:
                return order.find(c)
        
        s = list(s)
        s.sort(key=customCmp)
        return "".join(s)
        