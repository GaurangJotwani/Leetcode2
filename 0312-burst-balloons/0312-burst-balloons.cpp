class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>>dp(n, vector<int>(n));
        
        for (int g = 0; g < n; g++) {
            
            for (int i = 0, j = g; j < n; i++, j++) {
                
                int max = INT_MIN;
                for (int k = i; k <= j; k++) {
                    int left = k == i ? 0 : dp[i][k - 1];
                    int right = k == j ? 0 : dp[k + 1][j];
                    int val = (i == 0 ? 1 : nums[i - 1]) * nums[k] * (j == n - 1 ? 1 : nums[j + 1]);
                    int total = left + right + val;
                    if (total > max) max = total;
                    
                }
                
                dp[i][j] = max;
            }
        }
        
        
        
        
        return dp[0][n - 1];
    }
};