# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        d = defaultdict(list)
        minim = [0]
        maxim = [0]

        def dfs(node, col, depth):
            if not node:
                return
            d[col].append((depth,node.val))
            minim[0] = min(minim[0], col)
            maxim[0] = max(maxim[0], col)
            dfs(node.left, col - 1, depth + 1)
            dfs(node.right, col + 1, depth + 1)
        
        dfs(root, 0, 0)
        res = []
        for i in range(minim[0], maxim[0] + 1):
            lst = d[i]
            lst.sort()
            res.append([val for depth,val in lst])
        
        return res
        