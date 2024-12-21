class UndergroundSystem:

    def __init__(self):
        self.checkInTimes = defaultdict(list)
        self.checkoutTimes = {}
        self.averageTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInTimes[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_start, t_start = self.checkInTimes[id]
        self.checkInTimes[id] = []
        if (station_start, stationName) not in self.averageTimes:
            self.averageTimes[(station_start, stationName)] = [0,0]
        self.averageTimes[(station_start, stationName)][0] += t - t_start
        self.averageTimes[(station_start, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self.averageTimes[(startStation, endStation)]
        return total / cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)