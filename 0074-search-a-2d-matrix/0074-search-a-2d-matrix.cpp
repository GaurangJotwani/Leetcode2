class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0;
        int col = matrix[0].size() - 1;

        while (col >= 0 && row < matrix.size()) {
            int cNum = matrix[row][col];
            if (target == cNum) return true;
            if (target > cNum) {
                row++;
            } else {
                col--;
            }
        }
        return false;
    }
};