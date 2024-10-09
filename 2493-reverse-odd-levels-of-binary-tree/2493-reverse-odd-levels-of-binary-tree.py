# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
    
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Collect nodes of the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse values for odd levels
            if level % 2 == 1:
                # Collect values, reverse them, and reassign to the nodes
                values = [node.val for node in current_level]
                values.reverse()
                for i, node in enumerate(current_level):
                    node.val = values[i]
            
            level += 1
        
        return root