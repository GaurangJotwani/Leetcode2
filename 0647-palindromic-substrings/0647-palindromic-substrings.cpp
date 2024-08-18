class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, 0));

        for (int l = 1; l <= n; l++) {
            int j = l - 1;
            for (int i = 0; i < n - l + 1; i++) {
                if (l == 1) dp[i][j] = true;
                else if (l == 2) dp[i][j] = s[i] == s[j];
                else {
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]; 
                }
                j++;
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (dp[i][j]) res++;
            }
        }
        return res;
    }
};