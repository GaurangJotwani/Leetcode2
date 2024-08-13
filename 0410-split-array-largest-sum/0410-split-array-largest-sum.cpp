class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> dp(k + 1, vector<int>(n, INT_MIN));
        int sm = 0;
        for (int i = n - 1; i >= 0; i--) {
            sm += nums[i];
            dp[1][i]= sm;
        }

        for (int i = 2; i <= k; i++) {
            for (int j = n - i; j >= 0; j--) {
                int sm = 0;
                int minVal = INT_MAX;
                for (int x = j; x < n - i + 1; x++) {
                    sm += nums[x];
                    int secVal = dp[i - 1][x + 1];
                    int maxVal = max(secVal, sm);
                    minVal = min(minVal, maxVal); 
                }
                dp[i][j] = minVal;
            }
            
        }
        return dp[k][0];
        
    }
};