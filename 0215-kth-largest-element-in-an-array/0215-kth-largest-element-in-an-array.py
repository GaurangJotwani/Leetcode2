class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        minH = []

        for num in nums:
            heappush(minH, num)
            if len(minH) > k:
                heappop(minH)
        
        return minH[0]