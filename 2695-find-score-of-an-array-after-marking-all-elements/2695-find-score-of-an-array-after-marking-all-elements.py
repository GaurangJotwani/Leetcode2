class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        marked = set()
        sm = 0
        min_heap = []

        for i,num in enumerate(nums):
            heappush(min_heap, (num, i))
        
        while min_heap:
            num,i = heappop(min_heap)
            if i in marked:
                continue
            sm += num
            marked.add(i)
            marked.add(i + 1)
            marked.add(i - 1)
        
        return sm