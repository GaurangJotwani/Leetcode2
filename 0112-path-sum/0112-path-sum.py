# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def dfs(node, cSum):
            if cSum == targetSum and not node.left and not node.right:
                return True

            if not node:
                return False
            
            ans = False
            if node.left:
                ans = ans or dfs(node.left, cSum + node.left.val)
            if node.right:
                ans = ans or dfs(node.right, cSum + node.right.val)
            
            return ans
            
        
        return dfs(root, root.val)


            
        