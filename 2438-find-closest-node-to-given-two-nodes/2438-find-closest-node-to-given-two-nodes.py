class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        vis1 = [-1 for i in range(len(edges))]
        vis2 = [-1 for i in range(len(edges))]

        def bfs(src, vis):
            q = deque()
            q.append((src, 0))
            vis[src] = 0
            
            while q:
                node, d = q.popleft()
                nei = edges[node]

                if nei != -1 and vis[nei] == -1:
                    q.append((nei, d + 1))
                    vis[nei] = d + 1
        
        bfs(node1, vis1)
        bfs(node2, vis2)

        res = -1
        max_d = float("inf")

        for i in range(len(vis1)):
            if vis1[i] != -1 and vis2[i] != -1:
                temp = max(vis1[i], vis2[i])
                if temp < max_d:
                    res = i
                    max_d = temp
        
        return res
            

        