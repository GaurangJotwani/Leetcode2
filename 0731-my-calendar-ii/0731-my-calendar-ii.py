class MyCalendarTwo:

    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.overlapping:
            if not (startTime >= e or endTime <= s):
                return False
        
        for s, e in self.non_overlapping:
            if not (startTime >= e or endTime <= s):
                self.overlapping.append((max(s, startTime),min(endTime, e)))
        
        self.non_overlapping.append((startTime, endTime))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)