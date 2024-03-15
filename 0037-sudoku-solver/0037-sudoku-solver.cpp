class Solution {

public:
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
private: 
    bool solve(vector<vector<char>>& board) {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                   for (int i = 1; i < 10; i++) {
                       if (isSafe(r, c, i, board)) {
                           board[r][c] = '0' + i;
                           if (solve(board)) {
                               return true;
                           }
                           
                           board[r][c] = '.';
                       }
                   }
                   return false; 
                } 
            }
        }
        
        return true;
    }
    
    bool isSafe(int r, int c, int num, vector<vector<char>>& board) {
        char ch = '0' + num;
        for (int i = 0; i < 9; i++) {
            if (board[r][i] == ch) return false;
            if (board[i][c] == ch) return false;
            
            if (board[3*(r/3) + i/3][3*(c/3) + i%3] == ch) return false;
        }
        
        return true;
    }
};