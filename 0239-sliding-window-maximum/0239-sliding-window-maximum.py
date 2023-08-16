class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        q = deque()
        res = []
        
        for idx, num in enumerate(nums):
            
            while q and q[-1][0] < num:
                q.pop()
            
            q.append((num, idx))
            
            if idx - q[0][1] == k:
                q.popleft()
                
            
            #Dont append res
            if idx + 1 < k:
                continue
            
            res.append(q[0][0])
        
        return res
        