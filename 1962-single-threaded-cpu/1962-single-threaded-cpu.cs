public class Solution {
    public int[] GetOrder(int[][] tasks) {
        int n = tasks.Length;

        // Array to hold [enqueueTime, processingTime, index]
        int[][] indexedTasks = new int[n][];
        for (int taskIndex = 0; taskIndex < n; taskIndex++) {
            indexedTasks[taskIndex] = new int[] { tasks[taskIndex][0], tasks[taskIndex][1], taskIndex };
        }

        // Sort tasks by enqueue time
        Array.Sort(indexedTasks, (a, b) => a[0].CompareTo(b[0]));

        // Priority queue to select task based on processing time and then index
        var pq = new PriorityQueue<int[], int[]>(
            Comparer<int[]>.Create((x, y) => {
                if (x[0] != y[0]) return x[0].CompareTo(y[0]); // Compare processing time
                return x[1].CompareTo(y[1]); // If processing time is same, compare index
            })
        );

        var result = new List<int>();
        int time = 0, taskPtr = 0;

        // Process tasks
        while (taskPtr < n || pq.Count > 0) {
            // If no tasks are available to process, jump to the next available task's enqueueTime
            if (pq.Count == 0 && time < indexedTasks[taskPtr][0]) {
                time = indexedTasks[taskPtr][0];
            }

            // Add all tasks that are available by the current time to the priority queue
            while (taskPtr < n && indexedTasks[taskPtr][0] <= time) {
                pq.Enqueue(new int[] { indexedTasks[taskPtr][1], indexedTasks[taskPtr][2] }, new int[] { indexedTasks[taskPtr][1], indexedTasks[taskPtr][2] });
                taskPtr++;
            }

                var task = pq.Dequeue();
                result.Add(task[1]);  // Add task index to result
                time += task[0];  // Move the current time forward by the task's processing time
        }

        return result.ToArray();
    }
}
