# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        res = [None for _ in range(k)]
        if not head:
            return res
        
        l = self.getLength(head)
        
        # if k > l:
        #     curr = head
        #     for i in range(k):
        #         res[i] = ListNode(curr.val)
        #         curr = curr.next
        #         if not curr:
        #             break
        #     return res
        
        normal_case = l // k
        extra = l % k
        current_part = 0
        curr = head
        
        while curr:
            newList = ListNode(0)
            dummy = newList
            if extra == 0:
                for i in range(normal_case):
                    newNode = ListNode(curr.val)
                    newList.next = newNode
                    newList = newList.next
                    curr = curr.next
            else:
                for i in range(normal_case + 1):
                    newNode = ListNode(curr.val)
                    newList.next = newNode
                    newList = newList.next
                    curr = curr.next
                extra -= 1
            res[current_part] = dummy.next
            current_part += 1
        
        return res
                
                
                
                
            
            
    
    
    def getLength(self, head):
        
        ans = 0
        curr = head
        while curr:
            ans += 1
            curr = curr.next
        return ans
        