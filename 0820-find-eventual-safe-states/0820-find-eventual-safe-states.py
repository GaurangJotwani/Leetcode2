class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visiting = set()
        visited = set()
        res = []

        def dfs(node):
            visiting.add(node)

            for nei in graph[node]:
                if nei in visited:
                    continue
                if nei in visiting:
                    return False
                if not dfs(nei):
                    return False
            
            res.append(node)
            visited.add(node)
            return True

        
        for i in range(len(graph)):
            if i not in visited:
                dfs(i)
        
        return sorted(res)


        