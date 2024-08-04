class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        const int cnt = 9;
        vector<vector<bool>> rows(cnt, vector<bool>(cnt, false));
        vector<vector<bool>> cols(cnt, vector<bool>(cnt, false));
        vector<vector<bool>> areas(cnt, vector<bool>(cnt, false));

        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[0].size(); c++) {
                if (board[r][c] == '.') continue;

                int idx = board[r][c] - '0' -1;
                int area = (r / 3) * 3 + (c / 3);

                if (rows[r][idx] || cols[c][idx] || areas[area][idx]) return false;

                rows[r][idx] = true;
                cols[c][idx] = true;
                areas[area][idx] = true;
            }
        }
        return true;
    }
};