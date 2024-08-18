class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, 0));
        int res = 0;

        for (int l = 1; l <= n; l++) {
            int j = l - 1;
            for (int i = 0; i < n - l + 1; i++) {
                if (l == 1) dp[i][j] = true;
                else if (l == 2) dp[i][j] = s[i] == s[j];
                else dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1];
                res += dp[i][j];
                j++;
            }
        }

        return res;
    }
};