class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        ROWS,COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            heappush(min_heap, (matrix[r][0],r,0))
        
        while min_heap:
            # print(min_heap, k)
            num,r,c = heappop(min_heap)
            k -= 1
            if k == 0:
                return 1 * num
            if c == COLS - 1:
                continue
            heappush(min_heap, (matrix[r][c+1],r,c+1))
