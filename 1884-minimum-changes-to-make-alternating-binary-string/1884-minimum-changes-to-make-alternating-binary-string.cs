public class Solution {
    public int MinOperations(string s) {
        int n = s.Length;
        var oneFirst = new List<char>();
        var zeroFirst = new List<char>();
        char s1 = '1', s0 = '0';

        for (int i = 0; i < n; i++) {
            oneFirst.Add(s1);
            zeroFirst.Add(s0);
            s1 = s1 == '1' ? '0' : '1';
            s0 = s0 == '1' ? '0' : '1';
        }

        int minS1 = 0, minS2 = 0;

        for (int i = 0; i < n; i++) {
            if (s[i] != oneFirst[i]) minS1++;
            if (s[i] != zeroFirst[i]) minS2++;
        }

        return Math.Min(minS1, minS2);

    }
}