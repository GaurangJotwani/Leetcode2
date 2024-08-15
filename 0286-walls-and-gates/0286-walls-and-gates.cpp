class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
       int ROWS = rooms.size();
       int COLS = rooms[0].size();
       
       vector<vector<int>> dir = {{1, 0},{-1, 0},{0, 1},{0, -1}}; 
       vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));
       queue<pair<int, int>> q;
       for (int r = 0; r < ROWS; r++) {
        for (int c = 0; c < COLS; c++) {
            if (!visited[r][c] and rooms[r][c] == 0) {
                q.push({r, c});
                visited[r][c] = true;
            }
        }
       }
       while (!q.empty()) {
        int r = q.front().first;
        int c = q.front().second;
        q.pop();
        int dis = rooms[r][c];
        for (auto d: dir) {
            int row = r + d[0];
            int col = c + d[1];
            if (row >= 0 && row < ROWS && col < COLS && col >= 0 && !visited[row][col] && rooms[row][col] == INT_MAX) {
                visited[row][col] = true;
                q.push({row, col});
                rooms[row][col] = dis + 1;
            }
        }
       }

    


    }
};