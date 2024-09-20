class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        res = [float("inf")]
        adjList = defaultdict(list)
        for road in roads:
            adjList[road[0]].append((road[1], road[2]))
            adjList[road[1]].append((road[0], road[2]))

        vis = set()
        def dfs(node):
            vis.add(node)

            for nei,wt in adjList[node]:
                res[0] = min(res[0], wt)
                if nei not in vis:
                    dfs(nei)
        
        dfs(1)

        return res[0]
