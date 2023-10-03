"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        
        clones = {}
        
        if not node: return None
        def dfs(n):
            if n in clones:
                return clones[n]
            
            new_node = Node(n.val)
            clones[n] = new_node
            
            for nei in n.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            
            
            return new_node
        
        
        return dfs(node)
            
            
            
            
            
            
            
        