class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnts = Counter(nums)
        minHeap = []
        for key,val in cnts.items():
            if len(minHeap) < k:
                heappush(minHeap, (val, key))
            else:
                if minHeap[0][0] < val:
                    heappop(minHeap)
                    heappush(minHeap, (val, key))
        
        output = []
        while minHeap:
            output.append(minHeap[0][1])
            heappop(minHeap)
        
        return output
                

