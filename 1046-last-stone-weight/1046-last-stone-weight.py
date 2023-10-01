class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = []
        
        for num in stones:
            heapq.heappush(maxHeap, -1 * num)
        
        while len(maxHeap) > 1:
            biggest = -1 * heapq.heappop(maxHeap)
            smallest = -1 * heapq.heappop(maxHeap)
            
            diff = biggest - smallest
            if diff != 0:
                heapq.heappush(maxHeap, -1 * diff)
        
        if len(maxHeap) == 0: return 0
        else: return -1 * maxHeap[0]
        