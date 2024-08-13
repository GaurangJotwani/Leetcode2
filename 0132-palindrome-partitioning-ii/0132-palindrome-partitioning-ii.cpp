class Solution {
public:
    bool isPalindrome(string &s, int i, int j) {
        while (i <= j) {
            if (s[i] != s[j]) return false;
            i++;
            j--;
        }
        return true;
    }
    int minCut(string s) {
        int n = s.size();
        vector<int> dp(n + 1, INT_MAX);
        dp[n] = -1;
        vector<vector<bool>> memo(n, vector<bool>(n, false));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                memo[i][j] = isPalindrome(s, i, j);
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            int ans = INT_MAX;
            for (int j = i; j < n; j++) {
                if (memo[i][j]) {
                    ans = min(ans, 1 + dp[j + 1]);
                }
            }
            dp[i] = ans;
        }
        return dp[0];
    }
};