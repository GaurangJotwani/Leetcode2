class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> dp(nums.size(), 1);
        int c_max = 1;
        for (int i = 0; i < nums.size(); i++) {
            int a = nums[i];
            for (int j = 0; j < i; j++) {
                int b = nums[j];
                if (a % b == 0) {
                    dp[i] = max(dp[i], 1 + dp[j]);
                }
            }
            c_max = max(c_max, dp[i]);
        }
        
        vector<int> res;
        int prev = -1;
        // return dp;
        
        for (int i = dp.size() - 1; i >= 0; i--) {
            if(dp[i] == c_max) {
                if (prev == -1 || prev % nums[i] == 0) {
                    res.push_back(nums[i]);
                    c_max--;
                    prev = nums[i];
                    if (c_max == 0) return res;
                }
            }
        }
        
        return res;
    }
};