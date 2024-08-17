class Solution {
public:
    string longestPalindrome(string s) {
        vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), 0));

        for (int len = 1; len <= s.size(); len++) {
            int j = len - 1;
            for (int i = 0; i < s.size() - len + 1; i++) {
                if (len == 1) dp[i][j] = true;
                else if (len == 2) dp[i][j] = s[i] == s[j];
                else {
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1];
                }
                j++;
            }
        }

        string res = s.substr(0, 1);
        int val = 1;


        for (int i = 0; i < s.size(); i++) {
            for (int j = i + 1; j < s.size(); j++) {
                if (dp[i][j]) {
                    if (j - i + 1 > val) {
                        val = j - i + 1;
                        res = s.substr(i, j - i + 1);
                    }
                } 
            }
        }
        return res;
    }
};