# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []

        def findLeaves(root, leaves):
            if not root:
                return 
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            
            
            findLeaves(root.left, leaves)
            findLeaves(root.right, leaves)
        
        findLeaves(root1, leaves1)
        findLeaves(root2, leaves2)
        if len(leaves1) != len(leaves2):
            return False
        
        for i in range(len(leaves1)):
            if leaves1[i] != leaves2[i]:
                return False
        
        return True
