class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        
        int n = cost.size();
        if (n == 1) return 0;
        vector<int> dp(n + 1);
        for (int i = 2; i < dp.size(); i++) {
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1]);
        }
        return dp[n];

    }
};