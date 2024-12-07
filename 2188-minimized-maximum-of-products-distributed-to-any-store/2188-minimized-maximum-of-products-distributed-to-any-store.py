class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        max_heap = [] #(q and type)

        for i,q in enumerate(quantities):
            heappush(max_heap, [-q,q, 1])
        
        for i in range(n - len(quantities)):
            score,q,c = heappop(max_heap)
            new_score = math.ceil(q / (c + 1))
            heappush(max_heap, [-1 * new_score,q, c + 1])

        return -1 * max_heap[0][0]









        