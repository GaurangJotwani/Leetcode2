class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colors = [-1 for i in range(len(graph))] #-1 no color, 0 red, 1 blue
        

        def dfs(node, color):
            colors[node] = color

            for nei in graph[node]:
                if colors[nei] == -1:
                    if not dfs(nei, not color):
                        return False
                elif colors[nei] == color:
                    return False
            
            return True
        

        for i in range(len(graph)):
            if colors[i] == -1:
                if not dfs(i, 0):
                    return False
        
        return True




        