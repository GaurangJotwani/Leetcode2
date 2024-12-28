# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> None:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:


        visited = set()
        target = [None]
        directions = {"L": (0,-1),"R": (0,1),"U": (1,0),"D": (-1,0)}
        reverse_directions = {"L": "R","R": "L","U": "D","D": "U"}

        def dfs(r,c):
            if master.isTarget():
                target[0] = (r, c)
            
            visited.add((r,c))

            for direction in directions:
                row, col = r + directions[direction][0], c + directions[direction][1]
                if (row, col) not in visited and master.canMove(direction):
                    master.move(direction)
                    dfs(row, col)
                    master.move(reverse_directions[direction])
        
        dfs(0, 0)

        if not target[0]:
            return -1
        

        q = deque()
        q.append((0,0,0))
        visited2 = set()
        visited2.add((0,0))

        while q:
            r,c,d = q.popleft()
            if (r,c) == target[0]:
                return d
            
            for direction in directions:
                row, col = r + directions[direction][0], c + directions[direction][1]
                if (row,col) not in visited:
                    continue
                visited.remove((row, col))
                q.append((row, col, d + 1))
        

                


            

            









        