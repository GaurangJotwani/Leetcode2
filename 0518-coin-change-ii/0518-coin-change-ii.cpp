class Solution {
public:
    int target;
    vector<int> coins;
    vector<vector<int>> dp;
    
    int change(int amount, vector<int>& coins) {
        this->coins = coins;
        this->target = amount;
        dp = vector<vector<int>>(coins.size(), vector<int>(amount + 1, -1));
        return helper(0, 0);
    }

    int helper(int idx, int cSum) {
        if (cSum == target) return 1;
        if (idx == coins.size()) return 0;
        if (dp[idx][cSum] != -1) return dp[idx][cSum];
        int ans = 0;
        // include
        if (cSum + coins[idx] <= target) {
            ans += helper(idx, cSum + coins[idx]);
        }
        // exclude
        ans += helper(idx + 1, cSum);
        return dp[idx][cSum] = ans;
    }
};