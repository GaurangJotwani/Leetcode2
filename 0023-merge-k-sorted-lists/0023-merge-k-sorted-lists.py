# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        while len(lists) >= 2:
            l1 = lists.pop()
            l2 = lists.pop()
            merged = self.merge(l1, l2)
            lists.append(merged)
        
        return lists[0]

    def merge(self, l1, l2):
        dmy = ListNode()
        curr = dmy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return dmy.next
