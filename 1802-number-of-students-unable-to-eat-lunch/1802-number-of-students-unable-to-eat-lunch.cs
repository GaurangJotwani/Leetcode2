public class Solution {
    public int CountStudents(int[] students, int[] sandwiches) {
        var counts = new Dictionary<int,int>();
        int n = sandwiches.Length;
        foreach (var num in students) {
            if (counts.ContainsKey(num)) counts[num]++;
            else counts[num] = 1;
        }

        int s1 = 0;
        while (s1 < n) {
            int top = sandwiches[s1];
            if (counts.ContainsKey(top) && counts[top] > 0) {
                counts[top]--;
                s1++;
                continue;
            } return n - s1;
        }

        return 0;


    }
}