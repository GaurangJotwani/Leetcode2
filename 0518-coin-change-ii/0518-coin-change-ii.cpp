class Solution {
public:
    int target;
    vector<int> coins;
    
    int change(int amount, vector<int>& coins) {
        this->coins = coins;
        this->target = amount;
        vector<vector<int>> dp(coins.size(), vector<int>(amount + 1, -1));
        return helper(0, 0, dp);
    }

    int helper(int idx, int cSum, vector<vector<int>> &dp) {
        if (cSum == target) return 1;
        if (idx == coins.size()) return 0;
        if (dp[idx][cSum] != -1) return dp[idx][cSum];
        int ans = 0;
        // include
        if (cSum + coins[idx] <= target) {
            ans += helper(idx, cSum + coins[idx], dp);
        }
        // exclude
        ans += helper(idx + 1, cSum, dp);
        return dp[idx][cSum] = ans;
    }
};