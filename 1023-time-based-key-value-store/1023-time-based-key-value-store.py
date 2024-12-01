class TimeMap:

    def __init__(self):

        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        return self.binary_search(key, timestamp)
        
    def binary_search(self, key, timestamp):
        lst = self.d[key]
        res = ""
        l = 0
        r = len(lst) - 1

        while l <= r:
            mid = (l + r) // 2
            if lst[mid][0] <= timestamp:
                res = lst[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)