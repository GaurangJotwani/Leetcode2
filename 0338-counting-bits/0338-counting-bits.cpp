class Solution {
public:
    vector<int> countBits(int n) {
        if (n == 0) return {0};
        int curr = 1;
        int nxt = 2;
        vector<int>dp(n + 1, 0);
        dp[1] = 1;
        for (int i = 2; i < n + 1; i++) {
            if (i == nxt) {
                dp[i] = 1;
                curr = nxt;
                nxt = nxt << 1;
            } else {
                dp[i] = 1 + dp[i - curr];
            }
        }
        return dp;

    }
};