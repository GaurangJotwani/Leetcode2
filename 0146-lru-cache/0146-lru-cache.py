class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.tail.prev = self.head
        self.head.nxt = self.tail
        self.capacity = capacity

    
    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
    
    def add(self, node):
        prevNode = self.tail.prev
        prevNode.nxt = node
        node.prev = prevNode
        node.nxt = self.tail
        self.tail.prev = node 

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.remove(node)
        self.add(node)
        return self.d[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        node = ListNode(key, value)
        self.add(node)
        self.d[key] = node
        if len(self.d) > self.capacity:
            node_to_remove = self.head.nxt
            del self.d[node_to_remove.key]
            self.remove(node_to_remove)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)