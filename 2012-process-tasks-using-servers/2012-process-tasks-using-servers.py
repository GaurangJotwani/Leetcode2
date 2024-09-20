class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        n = len(tasks)
        ans = [-1] * n
        available = []
        unavailable = []
        for server, wt in enumerate(servers):
            heapq.heappush(available, (wt, server))
        time = 0
        task_index = 0

        while task_index < n:
            if not available:
                time = unavailable[0][0]
            # Push servers back to available if their busy time has elapsed
            while unavailable and unavailable[0][0] <= time:
                _, weight, index = heappop(unavailable)
                heappush(available, (weight, index))

            # If tasks can be assigned now, do it
            while available and task_index < n and task_index <= time:
                weight, index = heappop(available)
                heappush(unavailable, (time + tasks[task_index], weight, index))
                ans[task_index] = index
                task_index += 1

            # If no servers are available, fast-forward time to when the next server becomes available
        
            time += 1

        return ans






        