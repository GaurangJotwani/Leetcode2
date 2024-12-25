"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            nd = Node(insertVal)
            nd.next = nd
            return nd
        
        curr = head
                    
        while curr:
            if insertVal >= curr.val and insertVal <= curr.next.val:
                break
            
            if curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break
            if curr.next == head:
                break
            
            curr = curr.next
        
        nxt = curr.next
        curr.next = Node(insertVal)
        curr.next.next = nxt

        return head
