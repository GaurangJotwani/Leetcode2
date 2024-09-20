class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        incoming = [0] * numCourses
        prereqs = [{i} for i in range(numCourses)]
        adjList = defaultdict(list)

        for pre, crs in prerequisites:
            adjList[pre].append(crs)
            incoming[crs] += 1
        
        q = deque()
        for i,num in enumerate(incoming):
            if num == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for nei in adjList[node]:
                incoming[nei] -= 1
                for pre in prereqs[node]:
                    prereqs[nei].add(pre)
                if incoming[nei] == 0:
                    q.append(nei)
        
        res = []
        for u, v in queries:
            if u in prereqs[v]:
                res.append(True)
            else:
                res.append(False)
        
        return res



        