class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
      int ROWS = grid.size();
    int COLS = grid[0].size();
    
    // See if rows need to be flipped
    for (int i = 0; i < ROWS; i++) {
        if (grid[i][0] == 0) {
            flipRow(i, COLS, grid);
        }
    }
    
    for (int i = 0; i < COLS; i++) {
        if (ZeroMoreThanOnes(i, ROWS, grid)) {
            flipCol(i, ROWS, grid);
        }
    }
    
    int sum = 0;
    for (int r = 0; r < ROWS; r++) {
        sum += calSumRow(r, COLS, grid);
    }
    
    return sum;  
    }
    
    void flipRow(int r, int COLS, vector<vector<int>> &grid) {
    for (int c = 0; c < COLS; c++) {
        if (grid[r][c] == 0) grid[r][c] = 1;
        else grid[r][c] = 0;
        }
    }

    void flipCol(int c, int ROWS, vector<vector<int>> &grid) {
        for (int r = 0; r < ROWS; r++) {
            if (grid[r][c] == 0) grid[r][c] = 1;
            else grid[r][c] = 0;
        }
    }

    int calSumRow(int r, int COLS, vector<vector<int>> &grid) {
        int res = 1;
        int sum = 0;
        for (int c = COLS - 1; c >= 0; c--) {
            sum += grid[r][c] * res;
            res = res * 2;
        }
        return sum;
    }

    bool ZeroMoreThanOnes(int c, int ROWS, vector<vector<int>> &grid) {
        int zeroCount = 0;
        int oneCount = 0;

        for (int r = 0; r < ROWS; r++) {
            if (grid[r][c] == 0) zeroCount++;
            else oneCount++;
        }

        return zeroCount > oneCount;
    }
};