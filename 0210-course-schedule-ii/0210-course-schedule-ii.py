class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        order = []
        visited = set()
        visiting = set()

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
            order.append(node)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []

        return order