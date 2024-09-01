public class Solution {
    public int MinSwaps(string s) {
        int res = 0;
        int cSum = 0;
        foreach (var c in s) {
            if (c == ']') cSum--;
            else cSum++;
            if (cSum < 0) res = Math.Min(cSum, res);
        }
        if (res == 0) return 0;
        double tmp = ((double)Math.Abs(res)) / 2;

        return (Math.Abs(res) + 1) / 2;
    }
}