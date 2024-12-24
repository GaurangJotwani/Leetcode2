class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        
        l, r = 1, max(nums)
        res = r
        while l <= r:
            potential = (l + r) // 2
            if self.canMinimize(nums, maxOperations, potential):
                res = potential
                r = potential -1
            else:
                l = potential + 1

        return res
    
    def canMinimize(self, nums, maxOperations, potential):

        for num in nums:
            if num <= potential:
                continue
            operations = math.ceil(num / potential) - 1
            if operations > maxOperations:
                return False
            maxOperations -= operations
        
        return maxOperations >= 0