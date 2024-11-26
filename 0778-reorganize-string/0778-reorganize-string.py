class Solution:
    def reorganizeString(self, s: str) -> str:
        
        minHeap = []
        ans = []
        cntr = Counter(s)
        # print(cntr)
        for key, val in cntr.items():
            heapq.heappush(minHeap, (-val, key))
        
        while len(minHeap) >= 2:
            freq1, key1 = heappop(minHeap)
            ans.append(key1)
            freq2, key2 = heappop(minHeap)
            ans.append(key2)
            freq1 += 1
            freq2 += 1
            if freq1 < 0:
                heappush(minHeap, (freq1, key1))
            if freq2 < 0:
                heappush(minHeap, (freq2, key2))
        
        # print(minHeap)
        # print(ans)
        if not minHeap:
            return "".join(ans)
        
        if -1 * minHeap[0][0] > 1:
            return ""
        
        ans.append(minHeap[0][1])
        return "".join(ans)

