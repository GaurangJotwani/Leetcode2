class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:


        max_heap = []

        for gift in gifts:
            heappush(max_heap, -gift)

        for i in range(k):
            num = -1 * heappop(max_heap)
            num = math.floor(math.sqrt(num))
            heappush(max_heap, -1 * num)
        
        
        return -1 * sum(max_heap)
        