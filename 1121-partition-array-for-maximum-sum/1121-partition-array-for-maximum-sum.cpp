class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        int dp[n + 1];
        memset(dp, 0, sizeof(dp));
        for (int i = n - 1; i >= 0; i--) {
            int val = INT_MIN;
            int mx = 0;
            for (int j = 1; j <= k; j++) {
                if (i + j > n) continue;
                mx = max(mx, arr[i + j - 1]);
                val = max(val, mx * j + dp[i + j]);
            }
            dp[i] = val;
        }
        return dp[0];
    }
};