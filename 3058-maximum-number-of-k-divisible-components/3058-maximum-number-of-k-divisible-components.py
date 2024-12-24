class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        

        adjList = defaultdict(list)

        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        res = [0]

        def dfs(cur, par):
            total = values[cur]

            for child in adjList[cur]:
                if child != par:
                    total += dfs(child, cur)
            
            if total % k == 0:
                res[0] += 1
            
            return total

        dfs(0,-1)

        return res[0]
