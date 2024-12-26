class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        q = deque()
        visited = set()
        ROWS = len(nums)

        q.append((0,0))
        visited.add((0,0))
        res = []

        while q:
            r,c = q.popleft()
            res.append(nums[r][c])

            row = nums[r]

            if c == 0:
                if r + 1 < ROWS and c < len(nums[r + 1]) and (r + 1, c) not in visited:
                    visited.add((r + 1, c))
                    q.append((r + 1, c))
            
            if c + 1 < len(row):
                visited.add((r, c + 1))
                q.append((r, c + 1))
        
        return res


