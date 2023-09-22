class ListNode:

    def __init__(self, key = -1, nxt = None):
        self.key = key
        self.next = nxt

class MyHashSet:

    def __init__(self):
        self.hash_set = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key % 1000        

    def add(self, key: int) -> None:
        cur = self.hash_set[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        cur = self.hash_set[self.hash(key)]
        prev = cur
        cur = cur.next
        while cur:
            if cur.key == key:
                break
            prev = prev.next
            cur = cur.next
        
        if cur and cur.key == key:
            prev.next = prev.next.next

        

    def contains(self, key: int) -> bool:
        cur = self.hash_set[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)