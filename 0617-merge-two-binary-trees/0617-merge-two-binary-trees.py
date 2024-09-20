# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            
            val1 = 0 if not node1 else node1.val
            val2 = 0 if not node2 else node2.val

            left1 = None if not node1 else node1.left
            left2 = None if not node2 else node2.left

            right1 = None if not node1 else node1.right
            right2 = None if not node2 else node2.right

            new_node = TreeNode(val1 + val2)

            new_node.left = dfs(left1, left2)
            new_node.right = dfs(right1, right2)

            return new_node
        
        return dfs(root1, root2)
            
        