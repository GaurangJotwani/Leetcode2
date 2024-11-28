# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        res = [None]


        def dfs(node):
            if not node:
                return (False, False)
            p_found = False
            q_found = False
            if node.val == p.val:
                p_found = True
            if node.val == q.val:
                q_found = True
            
            p1,q1 = dfs(node.left)
            p2,q2 = dfs(node.right)

            p_found = p_found or p1 or p2
            q_found = q_found or q1 or q2

            if p_found and q_found and res[0] == None:
                res[0] = node

            return (p_found, q_found)
        
        dfs(root)
        return res[0]






            
        