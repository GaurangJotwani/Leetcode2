class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (auto num: nums) sum += num;
        if (sum % 2 != 0 || nums.size() == 1) return false;
        int n = sum / 2;

        vector<vector<bool>> dp(nums.size(), vector<bool>(n + 1, false));
        for (int i = 0; i < nums.size(); i++) dp[i][0] = true;
        if (nums[0] <= n) {
            dp[0][nums[0]] = true;
        }
        
        for (int i = 1; i < nums.size(); i++) {
            for (int j = 0; j <= n; j++) {
                dp[i][j] = dp[i - 1][j];
                if (j - nums[i] >= 0) {
                    dp[i][j] = dp[i][j] || dp[i - 1][j - nums[i]];
                }
            }
        }
        return dp[nums.size() - 1][n];

    }
};