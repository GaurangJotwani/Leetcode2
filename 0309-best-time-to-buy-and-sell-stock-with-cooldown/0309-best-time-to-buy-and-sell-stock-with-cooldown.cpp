class Solution {
public:
    vector<int> prices;
    vector<vector<int>> dp;
    int helper(int idx, bool buy) {
        if (idx >= prices.size()) return 0;
        if (dp[idx][buy] != -1) return dp[idx][buy]; 
        int ans = 0;
        // buy
        if (buy) {
            ans = max(ans, -1 * prices[idx] + helper(idx + 1, !buy));
        } else {
            //sell
            ans = max(ans, prices[idx] + helper(idx + 2, !buy));
        }
        // do nothing
        ans = max(ans, helper(idx + 1, buy));
        return dp[idx][buy] = ans;
    }

    int maxProfit(vector<int>& prices) {
        this->prices = prices;
        dp = vector<vector<int>>(prices.size(), vector<int>(2, -1));
        return helper(0, true);
    }
};