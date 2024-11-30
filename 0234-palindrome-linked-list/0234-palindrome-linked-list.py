# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        size = self.findLen(head)
        curr = head
        for i in range(1, size // 2):
            curr = curr.next
        l2 = curr.next
        curr.next = None
        l2 = self.reverse(l2)
        l1 = head

        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True


    
    def findLen(self, head):
        curr = head
        cnt = 0
        while curr:
            cnt += 1
            curr = curr.next
        return cnt

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev