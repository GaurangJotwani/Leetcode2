public class Solution {
    public int BestClosingTime(string customers) {
        var cc = new List<int>();
        int prefix = 0;
        int n = customers.Length;
        for (int i = 0; i < n; i++) {
            cc.Add(prefix);
            if (customers[i] == 'Y') prefix++;
        }
        cc.Add(prefix);

        // Yeses = [0, 1, 2, 2, 3]
        // No's = [0, 0, 0, 1, 1]
        int res = 0;
        int val = int.MaxValue;

        for (int i = 0; i < n + 1; i++) {
            int rightP = cc[n] - cc[i];
            int leftP = i - cc[i];
            if (rightP + leftP < val) {
                res = i;
                val = rightP + leftP;
            }
        }
        return res;
        
        
    }
}