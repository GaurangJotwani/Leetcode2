class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        adjBlue = defaultdict(list)
        adjRed = defaultdict(list)

        for src, dst in redEdges:
            adjRed[src].append(dst)
        for src, dst in blueEdges:
            adjBlue[src].append(dst)

        res = [-1 for i in range(n)]

        visited = set()
        q = deque()
        visited.add((0, None))
        q.append((0, 0, None))

        while q:
            node, d, prev = q.popleft()
            if res[node] == -1:
                res[node] = d

            if prev != "RED":
                for nei in adjRed[node]:
                    if (nei, "RED") in visited:
                        continue
                    q.append((nei, d + 1, "RED"))
                    visited.add((nei, "RED"))
            
            if prev != "BLUE":
                for nei in adjBlue[node]:
                    if (nei, "BLUE") in visited:
                        continue
                    q.append((nei, d + 1, "BLUE"))
                    visited.add((nei, "BLUE"))
        
        return res






        