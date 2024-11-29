class HitCounter:

    def __init__(self):
        self.pq = []
        

    def hit(self, timestamp: int) -> None:
        if self.pq and self.pq[0][0] == timestamp:
            self.pq[0][1] += 1
            return

        heappush(self.pq, [timestamp, 1])

        if timestamp - self.pq[0][0] >= 300:            
            heappop(self.pq)
            
        

    def getHits(self, timestamp: int) -> int:
        while self.pq and timestamp - self.pq[0][0] >= 300:
            heappop(self.pq)
        
        hits = 0
        for t,h  in self.pq:
            hits += h
        return hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)