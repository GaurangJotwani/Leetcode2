public class Solution {
    public string FrequencySort(string s) {
        var counter = new Dictionary<char, int>();
        var maxHeap = new PriorityQueue<char,int>();
        foreach(char c in s) {
            if (counter.ContainsKey(c)) counter[c]++;
            else counter[c] = 1;
        }
        foreach (var kvp in counter) maxHeap.Enqueue(kvp.Key, -1 * kvp.Value);

        var sb = new StringBuilder("");
        while (maxHeap.Count != 0) {
            char c = maxHeap.Peek();
            maxHeap.Dequeue();
            for (int i = 0; i < counter[c]; i++) sb.Append(c);
        }
        return sb.ToString();



    }
}