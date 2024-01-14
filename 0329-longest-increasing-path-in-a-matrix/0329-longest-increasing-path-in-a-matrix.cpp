class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result = max(result, helper(i, j, -1, m, n, matrix));
            }
        }
        return result;
    }
private:
    map<pair<int, int>, int>dp;
    int helper(int i, int j, int prev, int m, int n, vector<vector<int>>& matrix) {
        if (i < 0 || i >= m || j < 0 || j >= n || matrix[i][j] <= prev) {
            return 0;
        }
        
        if (dp.find({i, j}) != dp.end()) {
            return dp[{i, j}];
        }
        
        int result = 1;
        result = max(result, 1 + helper(i + 1, j, matrix[i][j], m, n, matrix));
        result = max(result, 1 + helper(i - 1, j, matrix[i][j], m, n, matrix));
        result = max(result, 1 + helper(i, j + 1, matrix[i][j], m, n, matrix));
        result = max(result, 1 + helper(i, j - 1, matrix[i][j], m, n, matrix));
        
        dp[{i, j}] = result;
        return dp[{i, j}];
    }
};