class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:


        min_heap = []
        for i,num in enumerate(nums):
            heappush(min_heap, (num, i))
        

        for _ in range(k):
            num, i = heappop(min_heap)
            nums[i] *= multiplier
            heappush(min_heap, (num * multiplier, i))
        
        # while min_heap:
        #     num, i = heappop(min_heap)
        #     nums[i] = num
        
        return nums

            
        