class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for i in range(n)]
        idx = n - 1

        l, r = 0, n - 1

        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res[idx] = nums[r] ** 2
                r -= 1
            else:
                res[idx] = nums[l] ** 2
                l += 1
            
            idx -= 1
        
        return res
            
