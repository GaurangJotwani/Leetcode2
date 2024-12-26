class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        q = deque()
        ROWS = len(nums)

        q.append((0,0))
        res = []

        while q:
            r,c = q.popleft()
            res.append(nums[r][c])

            row = nums[r]

            if c == 0:
                if r + 1 < ROWS and c < len(nums[r + 1]):
                    q.append((r + 1, c))
            
            if c + 1 < len(row):
                q.append((r, c + 1))
        
        return res


