"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        copyHashMap = {None:None}
        
        curr = head
        dummy = Node(0)
        l = dummy
        while curr:
            newNode = Node(curr.val, None, None)
            copyHashMap[curr] = newNode
            l.next = newNode
            l = l.next
            curr = curr.next
        
        curr1 = head
        curr2 = dummy.next
        while curr1:
            curr2.random = copyHashMap[curr1.random]
            curr1 = curr1.next
            curr2 = curr2.next
        
        return dummy.next
            
            
        