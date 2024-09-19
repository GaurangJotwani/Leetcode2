class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key = lambda x: x[1], reverse = True)

        res, csum = 0, 0
        minheap = []

        for n1, n2 in pairs:
            csum += n1
            heapq.heappush(minheap, n1)


            if len(minheap) > k:
                csum -= heapq.heappop(minheap)
            
            if len(minheap) == k:
                res = max(res, n2 * csum)
            
        

        return res


        