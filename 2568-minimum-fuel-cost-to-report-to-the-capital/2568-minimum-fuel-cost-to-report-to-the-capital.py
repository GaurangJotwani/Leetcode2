class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        res = [0]
        adjList = defaultdict(list)
        for road in roads:
            adjList[road[0]].append(road[1])
            adjList[road[1]].append(road[0])
        
        def dfs(node, par):
            total_children = 0

            for nei in adjList[node]:
                if nei != par:
                    children = dfs(nei, node)
                    res[0] += ceil(children / seats)
                    total_children += children

            return total_children + 1
        
        dfs(0, -1)

        return res[0]


        