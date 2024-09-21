class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        adjList = defaultdict(list)
        incoming = [0] * (n + 1)
        
        for src,dst in trust:
            adjList[src].append(dst)
            incoming[dst] += 1
        
        ans = -1
        for i in range(1, n + 1):
            if len(adjList[i]) == 0 and incoming[i] == n - 1:
                return i
        
        return ans
