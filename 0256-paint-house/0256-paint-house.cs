public class Solution {
    public int MinCost(int[][] costs) {
        
        int n = costs.Length;
        int[,] dp = new int[n,3];
        dp[0,0] = costs[0][0];
        dp[0,1] = costs[0][1];
        dp[0,2] = costs[0][2];

        for (int r = 1; r < n; r++) {
            dp[r,0] = costs[r][0] + Math.Min(dp[r - 1, 1],dp[r - 1, 2]);
            dp[r,1] = costs[r][1] + Math.Min(dp[r - 1, 0],dp[r - 1, 2]);
            dp[r,2] = costs[r][2] + Math.Min(dp[r - 1, 1],dp[r - 1, 0]);
        }

        return Math.Min(dp[n - 1,0], Math.Min(dp[n - 1,2], dp[n - 1,1]));
    }
}