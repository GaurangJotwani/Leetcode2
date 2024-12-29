# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        res = [None]
        if not root:
            return []
        if not root.left and not root.right:
            return root
        
        cache = defaultdict(int)
        self.findDepth(root, 0, cache)
        max_depth = max(cache.keys())
        nodes_to_find = cache[max_depth]
        print(nodes_to_find)

        def dfs(node, depth):
            if not node:
                return 0
            
            nodes_found_left = dfs(node.left, depth + 1)
            nodes_found_right = dfs(node.right, depth + 1)
            print(nodes_found_left, nodes_found_right)
            is_max_depth_node = 1 if depth == max_depth else 0

            if nodes_found_left + nodes_found_right + is_max_depth_node == nodes_to_find and not res[0]:
                res[0] = node

            return nodes_found_left + nodes_found_right + is_max_depth_node
        
        dfs(root, 0)
        return res[0]
            
            


    
    def findDepth(self, root, depth, cache):
        if not root:
            return 0
        cache[depth] += 1
        self.findDepth(root.left, depth + 1, cache)
        self.findDepth(root.right, depth + 1, cache)

        