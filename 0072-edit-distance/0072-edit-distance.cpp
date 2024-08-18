class Solution {
public:
    int dp[501][501];
    int minDistance(string word1, string word2) {
        this->word1 = word1;
        this->word2 = word2;
        memset(dp, -1, sizeof(dp));
        return helper(0, 0);
    }
private:
    string word1;
    string word2;
    
    int helper(int i, int j) {

        if (i == word1.size() && j == word2.size()) return 0;
        if (i == word1.size()) return word2.size() - j;
        if (j == word2.size()) return word1.size() - i;
        if (dp[i][j] != -1) return dp[i][j]; 
        
        int ans = INT_MAX;

        if (word1[i] == word2[j]) {
            ans = helper(i + 1, j + 1);  
        } else {
            ans = min({ans, 1 + helper(i + 1, j), 1 + helper(i, j + 1), 1 + helper(i + 1, j + 1)});
        }
        return dp[i][j] = ans;
    }
};









