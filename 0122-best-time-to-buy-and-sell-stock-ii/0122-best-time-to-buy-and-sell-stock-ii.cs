public class Solution {
    public int MaxProfit(int[] prices) {
        int maxProfit = 0;
        int prev = int.MaxValue;
        foreach (int num in prices) {
            if (num > prev) {
                maxProfit += num - prev;
            }
            prev = num;
        }
        return maxProfit;
    }
}