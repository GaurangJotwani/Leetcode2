# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        dummyLeft = ListNode()
        dummyRight = ListNode()
        
        node = head
        left = dummyLeft
        right = dummyRight
        
        while node:
            
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next
            
            node = node.next
        
        
        
#         print(dummyLeft.next.val)
#         print(dummyLeft.next.next.val)
#         print(dummyLeft.next.next.next.val)
        
#         print(dummyRight.next.val)
#         print(dummyRight.next.next.val)
#         print(dummyRight.next.next.next.val)
        
        
        
        left.next = dummyRight.next
        right.next = None
        
        
        
        return dummyLeft.next
            
        
        
        