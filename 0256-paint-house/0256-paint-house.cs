public class Solution {
    public int MinCost(int[][] costs) {
        
        int n = costs.Length;
        int[,] dp = new int[2,3];
        dp[0,0] = costs[0][0];
        dp[0,1] = costs[0][1];
        dp[0,2] = costs[0][2];

        for (int r = 1; r < n; r++) {
            dp[1,0] = costs[r][0] + Math.Min(dp[0, 1],dp[0, 2]);
            dp[1,1] = costs[r][1] + Math.Min(dp[0, 0],dp[0, 2]);
            dp[1,2] = costs[r][2] + Math.Min(dp[0, 1],dp[0, 0]);

            dp[0,0] = dp[1,0];
            dp[0,1] = dp[1,1];
            dp[0,2] = dp[1,2];
        }

        return Math.Min(dp[0,0], Math.Min(dp[0,1], dp[0,2]));
    }
}