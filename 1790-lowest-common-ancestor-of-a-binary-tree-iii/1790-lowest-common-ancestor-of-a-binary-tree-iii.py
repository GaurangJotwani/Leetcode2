"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors_1 = set()
        curr = p
        while curr:
            ancestors_1.add(curr.val)
            curr = curr.parent
        curr = q
        while curr:
            if curr.val in ancestors_1:
                return curr
            curr = curr.parent
        
        
        

        