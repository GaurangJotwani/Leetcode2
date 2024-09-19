class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        minheap = []
        freq = Counter(arr)
        
        for key,val in freq.items():
            heapq.heappush(minheap, (val, key))
        
        while k > 0:
            f,num = heapq.heappop(minheap)
            if f <= k:
                k -= f
            else:
                return len(minheap) + 1
        


        return len(minheap)
            
