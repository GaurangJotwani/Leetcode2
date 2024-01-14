class Solution {
public:
    int minDistance(string word1, string word2) {
        
        return helper(word1, word2, 0, 0);
    }
private:
    map<pair<int, int>, int>dp;
    int helper(string word1, string word2, int i, int j) {
        
        if (i == word1.size()) return word2.size() - j;
        
        if (j == word2.size()) return word1.size() - i;
        
        if (dp.find({i ,j}) != dp.end()) return dp[{i, j}];
        
        if (word1[i] == word2[j]) {
            return helper(word1, word2, i+1, j+1);
        }
        
        int case1 = helper(word1, word2, i + 1, j + 1);
        int case2 = helper(word1, word2, i, j + 1);
        int case3 = helper(word1, word2, i + 1, j);
        
        dp[{i,j}] = 1 + min(min(case1, case2), case3);
        return dp[{i, j}];
        
    }
};