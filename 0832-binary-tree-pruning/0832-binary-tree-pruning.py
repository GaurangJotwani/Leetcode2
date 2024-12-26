# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == 0:
                node.left = None
            
            right = dfs(node.right)
            if right == 0:
                node.right = None
            
            return max(left,right,node.val)
        
        val = dfs(root)
        return root if val != 0 else None