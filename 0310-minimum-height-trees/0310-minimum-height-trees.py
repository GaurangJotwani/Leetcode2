class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adjList = defaultdict(list)
        for src,dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        edge_cnt = {}
        leaves = deque()

        for src, nei in adjList.items():
            if len(nei) == 1:
                leaves.append(src)
            edge_cnt[src] = len(nei)
        

        while leaves:
            if (n <= 2):
                return list(leaves)
            n -= len(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                for nei in adjList[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)
        
            


        