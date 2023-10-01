class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        
        for num in nums:
            if len(self.minHeap) == self.k:
                if num < self.minHeap[0]:
                    continue
                heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, num)
                  
        

    def add(self, val: int) -> int:
        if len(self.minHeap) == self.k:
            if val < self.minHeap[0]:
                return self.minHeap[0]
            else:
                heapq.heappop(self.minHeap)
                
        heapq.heappush(self.minHeap, val)
        
        return self.minHeap[0]
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)