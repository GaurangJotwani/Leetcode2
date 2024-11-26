class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visiting = set()
        visited = set()
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[pre].append(crs)

        def dfs(node):
            visiting.add(node)
            for nei in adjList[node]:
                if nei in visited:
                    continue
                if nei in visiting:
                    return False
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
        