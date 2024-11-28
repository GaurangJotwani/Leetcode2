# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [float("-inf")]

        def dfs(node):

            if not node:
                return 0

            if not node.left and not node.right:
                res[0] = max(res[0], node.val)
                return node.val
            
            left_longest = max(0,dfs(node.left))
            right_longest = max(0, dfs(node.right))

            #  middle
            res[0] = max(res[0], node.val + left_longest + right_longest)

            #along the way
            return max(node.val + left_longest, node.val + right_longest)
        
        dfs(root)
        return res[0]