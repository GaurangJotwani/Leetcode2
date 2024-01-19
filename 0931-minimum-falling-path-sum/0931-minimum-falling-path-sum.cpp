class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        
        int ROWS = matrix.size();
        int COLS = matrix[0].size();
        vector<int>directions{1, 0, -1};
        
        for (int r = ROWS - 2; r >= 0; r--) {
            for (int c = COLS - 1; c >= 0; c--) {
                int temp = INT_MAX;
                for (auto dir: directions) {
                    int col = c + dir;
                    if (col >= 0 && col < COLS) {
                        temp = min(temp, matrix[r + 1][col]);
                    }
                }
                matrix[r][c] += temp;
            }
        }
        
        int res = INT_MAX;
        for (int i = 0; i < COLS; i++) {
            res = min(res, matrix[0][i]);
        }
        return res;
    }
};