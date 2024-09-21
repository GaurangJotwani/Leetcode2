class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adjList = defaultdict(list)
        for i,edge in enumerate(edges):
            adjList[edge[0]].append((edge[1], succProb[i]))
            adjList[edge[1]].append((edge[0], succProb[i]))

        pq = []
        heapq.heappush(pq, (-1, start_node))
        vis = set()

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -1 * prob
            if node in vis:
                continue
            if node == end_node:
                return prob
            vis.add(node)

            for nei,prob2 in adjList[node]:
                if nei not in vis:
                    heapq.heappush(pq,(-1 * prob * prob2, nei))
        

        return 0

