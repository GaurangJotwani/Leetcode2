class Solution:
    def reorganizeString(self, s: str) -> str:
        
        if len(s) == 1: return s
        
        ans = []
        heap = []
        freq = Counter(s)
        
        for char, f in freq.items():
            heapq.heappush(heap, (-1 * f, char))
            
        print(heap)
            
        maxFreq = heap[0][0]
        
        print(maxFreq)
        
        if -1 * maxFreq > ceil(len(s) / 2): return ""
        
        while heap:
            
            f,c = heapq.heappop(heap)
            f = -1 * f
            if not ans or ans[-1] != c:
                ans.append(c)
                f -= 1
                if f != 0:
                    heapq.heappush(heap, (-1 * f, c))
            else:
                n_f,n_c = heapq.heappop(heap)
                n_f = -1 * n_f
                ans.append(n_c)
                n_f -= 1
                if n_f != 0:
                    heapq.heappush(heap, (-1 * n_f, n_c))
                heapq.heappush(heap, (-1 * f, c))
        
        return "".join(ans)
            
