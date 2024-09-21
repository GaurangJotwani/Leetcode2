# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        res = [float("inf")]

        def helper(root):
            ans = [root.val, root.val]
            if not root.left and not root.right:
                return ans

            if root.right:
                l1,r1 = helper(root.right)
                res[0] = min(res[0], abs(root.val - l1))
                ans[1] = r1
            
            if root.left:
                l1,r1 = helper(root.left)
                res[0] = min(res[0], abs(root.val - r1))
                ans[0] = l1
            
            return ans
        
        helper(root)
        return res[0]


            

        
        helper(root)
        return res[0]
        