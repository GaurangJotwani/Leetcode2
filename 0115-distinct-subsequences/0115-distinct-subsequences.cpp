class Solution {
public:
    string t;
    string s;
    int dp[1001][1001];
    int solve(int i, int j) {
        if (i == s.size() && j == t.size()) return 1;
        if (i == s.size()) return 0;
        
        if (dp[i][j] != -1) return dp[i][j];
        int ans = 0;
        if (s[i] == t[j]) ans += solve(i + 1, j + 1);
        ans += solve(i + 1, j);
        return dp[i][j] = ans;
    }

    int numDistinct(string s, string t) {
        this->t = t;
        this->s = s;
        memset(dp, - 1, sizeof(dp));
        return solve(0, 0);
    }
};