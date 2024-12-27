# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        root_l = [root.val]
        left = self.getLeftBoundry(root.left)
        leaves = self.getLeaves(root)
        right = self.getRightBoundry(root.right)
        return root_l + left + leaves + right
        
    def getLeftBoundry(self, root):
        
        res = []
        if not root:
            return res
        curr = root
        while curr:
            if not curr.left and not curr.right:
                return res
            res.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
        return res
    
    def getRightBoundry(self, root):
        res = []
        if not root:
            return res
        curr = root
        while curr:
            if not curr.left and not curr.right:
                break
            res.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        
        res.reverse()
        return res
    
    def getLeaves(self, root):
        res = []
        if not root:
            return []
        if not root.left and not root.right:
            return []
        
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                res.append(node.val)
                return
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res
        
        

        