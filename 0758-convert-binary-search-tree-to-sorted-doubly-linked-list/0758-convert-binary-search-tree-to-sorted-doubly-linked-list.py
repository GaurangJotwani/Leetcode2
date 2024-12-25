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
        nodes = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        
        dfs(root)

        for i in range(len(nodes)):
            cNode = nodes[i]
            if i - 1 >= 0:
                cNode.left = nodes[i - 1]
            if i + 1 < len(nodes):
                cNode.right = nodes[i + 1]
        
        nodes[0].left = nodes[-1]
        nodes[-1].right = nodes[0]

        return nodes[0]




        return root