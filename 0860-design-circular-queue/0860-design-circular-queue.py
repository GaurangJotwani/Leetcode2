class MyCircularQueue:

    def __init__(self, k: int):
        self.enqList = []
        self.deqList = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.enqList) + len(self.deqList) == self.k:
            return False 
        self.enqList.append(value)
        return True

    def deQueue(self) -> bool:
        if not self.deqList and not self.enqList:
            return False
        if self.deqList:
            self.deqList.pop()
            return True
        while self.enqList:
            self.deqList.append(self.enqList.pop())
        self.deqList.pop()
        return True

    def Front(self) -> int:
        if self.deqList:
            return self.deqList[-1]
        if self.enqList:
            return self.enqList[0]
        return -1

    def Rear(self) -> int:
        if self.enqList:
            return self.enqList[-1]
        if self.deqList:
            return self.deqList[0]
        return -1
        
        

    def isEmpty(self) -> bool:
        return not self.deqList and not self.enqList

    def isFull(self) -> bool:
        return len(self.enqList) + len(self.deqList) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()