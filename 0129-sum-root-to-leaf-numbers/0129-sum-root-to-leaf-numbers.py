# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = [0]
        def helper(node, cSum):
           
            cSum = cSum * 10 + node.val

            if not node.left and not node.right:    
                res[0] += cSum
                return
            
            if node.left:
                helper(node.left, cSum)
            
            if node.right:
                helper(node.right, cSum)
            
        helper(root, 0)
        return res[0]
            

            
        