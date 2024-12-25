class MovingAverage:

    def __init__(self, size: int):
        self.capacity = size
        self.elements = deque()
        self.cSum = 0
        

    def next(self, val: int) -> float:
        self.elements.append(val)
        self.cSum += val
        if len(self.elements) > self.capacity:
            self.cSum -= self.elements.popleft()
        
        return self.cSum / len(self.elements)



        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)