public class Solution {
    public int[] GetOrder(int[][] tasks) {
        // Priority Queue with custom comparison logic: first compare by processing time, then by index
        var pq = new PriorityQueue<int[], int[]>(
            Comparer<int[]>.Create((x, y) => {
                int cmp = x[0].CompareTo(y[0]); // Compare by processing time
                if (cmp == 0) return x[1].CompareTo(y[1]); // If processing time is the same, compare by index
                return cmp;
            })
        );

        // Add index to tasks array so that we can track the original order
        var indexedTasks = tasks
            .Select((task, index) => new int[] { task[0], task[1], index })  // [enqueueTime, processingTime, index]
            .OrderBy(t => t[0])  // Sort tasks by enqueueTime
            .ToArray();

        int i = 0, time = 0, n = tasks.Length;
        var result = new List<int>();

        // Process tasks
        while (i < n || pq.Count > 0) {
            // If no tasks are available to process, jump to the next available task's enqueueTime
            if (pq.Count == 0 && time < indexedTasks[i][0]) {
                time = indexedTasks[i][0];
            }

            // Add all tasks that are available by the current time 'time' to the priority queue
            while (i < n && indexedTasks[i][0] <= time) {
                pq.Enqueue(new int[] { indexedTasks[i][1], indexedTasks[i][2] }, new int[] { indexedTasks[i][1], indexedTasks[i][2] });
                i++;
            }

            // Process the task with the shortest processing time (and smallest index if there's a tie)
            if (pq.Count > 0) {
                var task = pq.Dequeue();
                result.Add(task[1]);  // Add task index to result
                time += task[0];  // Move the current time forward by the task's processing time
            }
        }

        return result.ToArray();
    }
}
