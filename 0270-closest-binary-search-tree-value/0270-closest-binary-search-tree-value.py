# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = float("inf")
        res = root.val

        while root:
            if abs(root.val - target) < diff:
                res = root.val
                diff = abs(root.val - target)
            
            if abs(root.val - target) == diff:
                res = min(root.val,res)
            
            if target == root.val:
                return root.val
            elif target > root.val:
                root = root.right
            else:
                root = root.left
        
        return res