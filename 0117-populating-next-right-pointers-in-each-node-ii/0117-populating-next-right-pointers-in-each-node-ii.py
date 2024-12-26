"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root

        leftmost = root

        while leftmost:
            curr = leftmost
            leftmost = prev = None
            while curr:
                if leftmost == None:
                    if curr.left:
                        leftmost = curr.left
                    elif curr.right:
                        leftmost = curr.right
                
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    prev = curr.left
                
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    prev = curr.right
                    
                curr = curr.next
        
        return root