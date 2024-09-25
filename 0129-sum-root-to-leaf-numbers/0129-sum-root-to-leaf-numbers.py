# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(node, cSum):
            cSum = cSum * 10 + node.val
            
            if not node.left and not node.right:    
                return cSum
            
            ans = 0
            
            if node.left:
                ans += helper(node.left, cSum)
            
            if node.right:
                ans += helper(node.right, cSum)
            
            return ans
            
        return helper(root, 0)
            

            
        