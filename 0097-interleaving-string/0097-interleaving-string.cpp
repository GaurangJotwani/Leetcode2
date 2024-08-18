class Solution {
public:
    string s1;
    string s2;
    string s3;
    vector<vector<int>> dp;

    bool helper(int i, int j) {
        if (i == s1.size() and j == s2.size()) return true;
        if(dp[i][j] != - 1) return dp[i][j];
        int k = i + j;
        bool ans = false;
        if (i < s1.size() and s1[i] == s3[k]) {
            ans = ans or helper(i + 1, j);
        }

        if (j < s2.size() and s2[j] == s3[k]) {
            ans = ans or helper(i, j + 1);
        }

        return dp[i][j] = ans;
    }

    bool isInterleave(string s1, string s2, string s3) {
        this->s1 = s1;
        this->s2 = s2;
        this->s3 = s3;
        if (s1.size() + s2.size() != s3.size()) return false;
        dp.resize(s1.size() + 1, vector<int>(s2.size() + 1, -1));
        return helper(0, 0); 
    }
};