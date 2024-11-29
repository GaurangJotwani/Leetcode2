# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        fast = head
        for i in range(n):
            fast = fast.next
        slow = head
        while fast != None:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        prev.next = slow.next

        return dummy.next