"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        if not root.left and not root.right:
            root.left = root
            root.right = root
            return root
        
        prev = [None]
        first = [None]

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if not first[0]:
                first[0] = node
            if prev[0]:
                prev[0].right = node
                node.left = prev[0]
            
            prev[0] = node
            dfs(node.right)
        
        dfs(root)
        first[0].left = prev[0]
        prev[0].right = first[0]
        return first[0]






