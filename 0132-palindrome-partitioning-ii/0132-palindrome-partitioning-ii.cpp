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
        vector<vector<bool>> isPalindrome(n, vector<bool>(n, false));
        vector<int> dp(n, INT_MAX);
        
        // Build the isPalindrome table
        for (int i = 0; i < n; i++) {
            isPalindrome[i][i] = true;  // Single characters are palindromes
        }
        for (int i = 0; i < n - 1; i++) {
            isPalindrome[i][i + 1] = (s[i] == s[i + 1]);  // Two consecutive characters
        }
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                isPalindrome[i][j] = (s[i] == s[j]) && isPalindrome[i + 1][j - 1];
            }
        }

        // Fill dp array
        for (int j = 0; j < n; j++) {
            if (isPalindrome[0][j]) {
                dp[j] = 0;
            } else {
                for (int i = 1; i <= j; i++) {
                    if (isPalindrome[i][j]) {
                        dp[j] = min(dp[j], dp[i - 1] + 1);
                    }
                }
            }
        }
        
        return dp[n - 1];
    }
};