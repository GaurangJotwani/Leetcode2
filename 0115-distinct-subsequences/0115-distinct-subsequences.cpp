class Solution {
public:
    map<pair<int, int>, int>dp;
    int numDistinct(string s, string t) {
        return helper(0, 0, s, t);
    }
private:
    int helper(int i, int j, string& s, string& t) {
        if (j == t.size()) return 1;
        if (i == s.size()) return 0;
        if (dp.find({i, j}) != dp.end()) {
            return dp[{i, j}];
        }
        
        
        if (s[i] == t[j]) {
            dp[{i, j}] = helper(i + 1, j + 1, s, t) + helper(i + 1, j, s, t);
        } else {
            dp[{i, j}] = helper(i + 1, j, s, t);
        }
        
        return dp[{i, j}];
    }
};