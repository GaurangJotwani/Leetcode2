class Solution {
public:
    bool isMatch(string s, string p) {
        
        
        int n = s.size();
        int m = p.size();
        
        vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
        
        cout << dp[n][m];
        
        for (int i = 0; i < m + 1; i++) {
            if (i == 0) {dp[0][i] = true;}
            else if (p[i - 1] == '*') dp[0][i] = dp[0][i - 2];
        }
        
        cout << dp[0][0] << " " << dp[0][m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (s[i] == p[j] || p[j] == '.') {
                    dp[i + 1][j + 1] = dp[i][j];
                } else if (p[j] == '*') {
                    if (dp[i + 1][j - 1]) dp[i + 1][j + 1] = true;
                    else if (p[j - 1] == s[i] || p[j - 1] == '.') dp[i + 1][j + 1] = dp[i][j + 1];
                } else {
                    dp[i + 1][j + 1] = false;
                }
            }
        }
        
        
        return dp[n][m];
    }
};