class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        output = 0

        cnt = Counter(tasks)
        minH = []
        notAvailable = []
        for key, val in cnt.items():
            heapq.heappush(minH ,(-1 * val, key))
        
        while minH or notAvailable:
            output += 1
            if not minH:
                output = notAvailable[0][0]
                
            while notAvailable and notAvailable[0][0] <= output:
                _, freq, key = heapq.heappop(notAvailable)
                heapq.heappush(minH, (freq, key))

            freq, key = heapq.heappop(minH)
            freq += 1
            if freq != 0:
                heapq.heappush(notAvailable, (output + n + 1, freq, key))
        
        return output


