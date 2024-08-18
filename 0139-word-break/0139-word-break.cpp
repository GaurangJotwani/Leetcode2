class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> mp;
        for (auto word: wordDict) mp.insert(word);

        int n = s.size();

        vector<bool> dp(n + 1, false);
        dp[n] = true;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                string sub = s.substr(i, j - i + 1);
                if (mp.find(sub) != mp.end()) {
                    int l = sub.size();
                    dp[i] = dp[i + l];
                    if (dp[i]) break;
                }
            }
        }
        return dp[0];
    }
};