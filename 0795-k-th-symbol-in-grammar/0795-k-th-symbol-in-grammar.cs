public class Solution {
    public int KthGrammar(int n, int k) {
        if (n == 1) return 0;
        int l = 1;
        int r = (1<<(n-1));
        int cAns = 0;

        for (int row = 2; row <= n; row++) {
            int mid = l + ((r - l) / 2);
            Console.WriteLine(l + " " + r + " " + k);
            
            if (k > mid) {
                if (cAns == 0) cAns = 1;
                else cAns = 0;
                l = mid + 1;
            } else {
                if (cAns == 0) cAns = 0;
                else cAns = 1;
                r = mid - 1;
            }
        }
        return cAns;
    }
}