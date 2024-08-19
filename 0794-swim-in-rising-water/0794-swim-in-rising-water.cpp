class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        vector<vector<int>> dir = {{0, 1},{0, -1},{1, 0},{-1, 0}};
        priority_queue<vector<int>, vector<vector<int>>, Comparator> pq;
        pq.push({grid[0][0], 0, 0});
        vector<vector<bool>> seen(ROWS, vector<bool>(COLS, false));
        while (!pq.empty()) {
            int r = pq.top()[1];
            int c = pq.top()[2];
            int w1 = pq.top()[0];
            pq.pop();
            if (seen[r][c]) continue;
            seen[r][c] = true;
            cout << w1 << " " << r << " " << c << endl;
            if (r == ROWS - 1 && c == COLS - 1) return w1;
            for (auto d: dir) {
                int row = r + d[0];
                int col = c + d[1];
                if (row >= 0 && row < ROWS && col >= 0 && col < COLS && !seen[row][col]) {
                    if (grid[row][col] <= w1) {
                        pq.push({w1, row, col});
                    } else {
                        int diff = grid[row][col] - w1;
                        //cout << diff << " " << w1 << endl;
                        pq.push({w1 + diff, row, col});
                    }
                }
            }
        }
        return -1;
    }
private:
    struct Comparator {
        bool operator()(vector<int>& v1,vector<int>& v2) {
            return v1[0] > v2[0];
        } 
    };
};