class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int size = prices.size();
        int index = 0;
        int canBuy = 1;
        vector<vector<int>> dp(size + 1, vector<int>(2, -1));
        
        return helper(index, canBuy, dp, prices);
    }
private:
    int helper(int i, int canBuy, vector<vector<int>> &dp, vector<int>& prices) {
        
        if (i >= prices.size()) {
            return 0;
        }
        
        if (dp[i][canBuy] != -1) {
            return dp[i][canBuy];
        }
        int val1;
        if (canBuy == 1) {
            val1 = -1 * prices[i] + helper(i + 1, 0, dp, prices);
        } else {
            val1 = prices[i] + helper(i + 2, 1, dp, prices);
        }
        
        int val2 = helper(i + 1, canBuy, dp, prices);
        
        dp[i][canBuy] = max(val1, val2);
        return dp[i][canBuy];
    }
};