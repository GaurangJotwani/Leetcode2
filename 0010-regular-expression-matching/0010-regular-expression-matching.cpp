class Solution {
public:
    string p;
    string s;
    int dp[21][21];

    bool isMatch(string s, string p) {
        this->s = s;
        this->p = p;
        memset(dp, -1, sizeof(dp));
        return helper(0, 0);        
    }

    bool helper(int i, int j) {
        if (j == p.size() & i == s.size()) return true;
        if (j == p.size()) return false;
        if (dp[i][j] != -1) return dp[i][j];
        bool ans = false;
        // case 1 *
        if (j + 1 < p.size() && p[j + 1] == '*') {
            // case 1a (include)
            if (i < s.size() && (s[i] == p[j] || p[j] == '.')) {
                ans = ans || helper(i + 1, j);
            }
            //case 1b exclude
            ans = ans || helper(i, j + 2);
        } else {
            if (i < s.size() && (s[i] == p[j] || p[j] == '.')) {
                ans = ans || helper(i + 1, j + 1);
            }
        }
        return dp[i][j] = ans;
    }

};












