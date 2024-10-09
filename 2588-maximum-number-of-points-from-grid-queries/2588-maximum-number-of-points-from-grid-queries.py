
# Approach
# Sort queries and process each with a BFS (or DFS), keeping track of visited cells, 
# to count accessible cells with values below the query.
# Use Min Heap so that we dont have to repeat BFS

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [0] * len(queries)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        max_heap = []
        heappush(max_heap, (grid[0][0], 0, 0))
        visited.add((0, 0))
        points = 0

        for q, idx in sorted_queries:
            while max_heap and max_heap[0][0] < q:
                val, x, y = heappop(max_heap)
                points += 1  # Add point for the cell
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        heappush(max_heap, (grid[nx][ny], nx, ny))
            result[idx] = points  # Store the result for each query

        return result

