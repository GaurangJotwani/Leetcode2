from sortedcontainers import SortedList

class StatisticsTracker:

    def __init__(self):
        self.q = deque()
        self.sl = SortedList()
        self.d = defaultdict(int)
        self.sm = 0

    def addNumber(self, number: int) -> None:
        self.q.append(number)
        self.sl.add(number)
        self.d[number] += 1
        self.sm += number

    def removeFirstAddedNumber(self) -> None:
        num = self.q.popleft()
        self.sm -= num
        self.d[num] -= 1
        if self.d[num] == 0:
            del self.d[num]
        self.sl.remove(num)

    def getMean(self) -> int:
        return math.floor(self.sm / len(self.q))

    def getMedian(self) -> int:
        if len(self.q) % 2 == 1:
            return self.sl[len(self.q) // 2]
        else:
            idx = len(self.q) // 2
            return self.sl[idx]


    def getMode(self) -> int:
        res = -1
        freq = float("-inf")

        for key,val in self.d.items():
            if val > freq:
                freq = val
                res = key
            elif val == freq and key < res:
                res = key
        return res



# Your StatisticsTracker object will be instantiated and called as such:
# obj = StatisticsTracker()
# obj.addNumber(number)
# obj.removeFirstAddedNumber()
# param_3 = obj.getMean()
# param_4 = obj.getMedian()
# param_5 = obj.getMode()