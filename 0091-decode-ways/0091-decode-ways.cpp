class Solution {
public:
    int numDecodings(string s) {
        if (s[0] == '0') return 0;
        
        int n = s.size();
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            int dig = s[i - 1] - '0';
            if (dig != 0) {
                dp[i] = dp[i - 1];
            }

            int prev_dig = s[i - 2] - '0';
            cout << prev_dig << endl;
            if (prev_dig == 1 or (prev_dig == 2 and dig <= 6)) {
                dp[i] += dp[i - 2];
            }
        }
        return dp[n];
    }
};











