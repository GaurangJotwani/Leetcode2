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
            new_lst = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged = self.merge(l1, l2)
                new_lst.append(merged)
            lists = new_lst
        
        return lists[0]

    def merge(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1

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
