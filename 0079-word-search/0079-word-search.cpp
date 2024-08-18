class Solution {
public:
    string word;
    int ROWS; 
    int COLS;
    vector<vector<char>> board;
    vector<vector<int>> dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    bool dfs(int r, int c, int idx) {
        // Base cases
        if (idx == word.size()) return true;
        if (r < 0 || r >= ROWS || c < 0 || c >= COLS || board[r][c] != word[idx]) return false;

        // Temporarily mark the cell as visited
        char temp = board[r][c];
        board[r][c] = '#'; // Use a special character to mark as visited

        // Explore all possible directions
        for (auto d : dir) {
            int row = r + d[0];
            int col = c + d[1];
            if (dfs(row, col, idx + 1)) return true;
        }

        // Restore the cell's original value
        board[r][c] = temp;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        this->word = word;
        ROWS = board.size();
        COLS = board[0].size();
        this->board = board;

        // Start DFS from every cell that matches the first letter of the word
        for (int r = 0; r < ROWS; ++r) {
            for (int c = 0; c < COLS; ++c) {
                if (board[r][c] == word[0] && dfs(r, c, 0)) return true;
            }
        }

        return false;
    }
};