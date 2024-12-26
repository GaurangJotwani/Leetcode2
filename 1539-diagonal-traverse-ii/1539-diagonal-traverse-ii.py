class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        groups = defaultdict(list)
        ROWS = len(nums)

        for r in range(ROWS - 1, -1, -1):
            for c in range(len(nums[r])):
                groups[r + c].append(nums[r][c])
        
        curr = 0
        res = []

        while curr in groups:
            res.extend(groups[curr])
            curr += 1
        
        return res