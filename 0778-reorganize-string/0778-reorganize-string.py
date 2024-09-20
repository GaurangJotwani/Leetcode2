class Solution:
    def reorganizeString(self, s: str) -> str:
        
        res = []
        pq = []
        freq = Counter(s)
        for key,val in freq.items():
            heapq.heappush(pq, (-val, key))

        while pq:
            print(res, pq)
            cnt, let = heapq.heappop(pq)

            if res and res[-1] == let:
                if not pq:
                    return ""
                cnt2, let2 = heapq.heappop(pq)
                heapq.heappush(pq, (cnt, let))
                res.append(let2)
                cnt2 += 1
                if cnt2 != 0:
                    heapq.heappush(pq, (cnt2, let2))
            
            else:
                res.append(let)
                cnt += 1
                if cnt != 0:
                    heapq.heappush(pq,(cnt, let))

        return "".join(res)