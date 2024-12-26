class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:


        minHeap = []

        for i,num in enumerate(arr):
            heappush(minHeap, (num, i))
        
        idx = 1

        while minHeap:
            c_val = minHeap[0][0]
            while minHeap and minHeap[0][0] == c_val:
                num,i = heappop(minHeap)
                arr[i] = idx
            
            idx += 1
        

        return arr
        