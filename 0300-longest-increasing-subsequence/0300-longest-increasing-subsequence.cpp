class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (nums.size() == 1) return 1;
        vector<int> dp(n, 1);
        int res = 0;
        for (int i = 1; i < n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], 1 + dp[j]);
                }
            }
            res = max(res, dp[i]);
        }
        return res;
    }
};