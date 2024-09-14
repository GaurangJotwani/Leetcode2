public class Solution {
    public int SumSubarrayMins(int[] arr) {
        long res = 0;
        long mod = 1000000007;
        var stk = new Stack<(int num, int l, int r)>();
        stk.Push((arr[0], 0, 0));
        for (int i = 1; i < arr.Length; i++) {
            int num = arr[i];
            int curIdx = i;
            while (stk.Count > 0 && stk.Peek().num > num) {
                curIdx = stk.Peek().l;
                int left = stk.Peek().r - stk.Peek().l + 1;
                int right = i - stk.Peek().r;
                long tmp = ((long)left * right) * stk.Peek().num;
                res = (res + tmp) % mod;
                
                stk.Pop();
            }
            stk.Push((num, curIdx, i));
        }
        while (stk.Count > 0) {
                int left = stk.Peek().r - stk.Peek().l + 1;
            int right = arr.Length - stk.Peek().r;
            
            long tmp = ((long)left * right) * stk.Peek().num;
            res = (res + tmp) % mod;

            stk.Pop();
        }

        return (int) res;
    }
}