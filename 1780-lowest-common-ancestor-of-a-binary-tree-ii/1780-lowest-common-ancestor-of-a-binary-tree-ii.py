# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        res = [None]
        def dfs(root):
            if not root:
                return [False, False]
            
            p_found = root.val == p.val
            q_found = root.val == q.val
            
            #Leaf node
            if not root.left and not root.right:
                return [p_found, q_found]
            
            p_left, q_left = dfs(root.left)
            p_right, q_right = dfs(root.right)

            p_found = p_found or p_left or p_right
            q_found = q_found or q_left or q_right

            if p_found and q_found and not res[0]:
                res[0] = root
            
            return [p_found, q_found]
        
        dfs(root)
        return res[0]



        