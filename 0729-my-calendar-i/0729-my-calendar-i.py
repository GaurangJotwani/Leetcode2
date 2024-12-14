class TreeNode:
    def __init__(self, start, end, left = None, right = None):
        self.left = left
        self.right = right
        self.start = start
        self.end = end

class BST:
    def __init__(self,start, end):
        self.root = TreeNode(start, end)
    
    def book(self,start, end):
        curr = self.root
        while curr:
            if not (end <= curr.start or start >= curr.end):
                return False
            if start >= curr.end:
                if not curr.right:
                    curr.right = TreeNode(start, end)
                    return True
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = TreeNode(start,end)
                    return True
                curr = curr.left
        
class MyCalendar:

    def __init__(self):
        self.bst = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.bst:
            self.bst = BST(startTime, endTime)
            return True
        return self.bst.book(startTime, endTime)
    


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)