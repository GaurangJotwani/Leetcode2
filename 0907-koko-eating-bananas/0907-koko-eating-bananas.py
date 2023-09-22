class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        ans = right

        while left <= right:

            mid = (left + right) // 2
            if self.canEat(piles, h, mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
                
    

    def canEat(self, piles, h, pace):

        total_h = 0

        for pile in piles:
            total_h += ceil(pile / pace)
        
        if total_h <= h:
            return True
            
        