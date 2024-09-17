class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = defaultdict(list)
        
        # Build the adjacency list, marking the direction of the roads.
        for a, b in connections:
            adjList[a].append((b, 1))  # 1 indicates a road from a -> b
            adjList[b].append((a, 0))  # 0 indicates a road from b -> a
        
        visit = set()
        res = [0]
        
        def dfs(node):
            visit.add(node)
            for nei, need_reverse in adjList[node]:
                if nei not in visit:
                    # If the road goes away from 0 (need_reverse == 1), we need to reverse it.
                    res[0] += need_reverse
                    dfs(nei)

        # Start DFS from the capital city (node 0)
        dfs(0)
        
        return res[0]
