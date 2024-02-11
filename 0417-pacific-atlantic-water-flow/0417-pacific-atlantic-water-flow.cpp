class Solution {
public:
    int ROWS;
    int COLS;
    vector<vector<int>> h;
    vector<vector<int>> dir = {{1, 0},{-1, 0},{0, 1},{0, -1}};
    
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        ROWS = heights.size();
        COLS = heights[0].size();
        h = heights;
        
        map<pair<int, int>, bool> pac;
        map<pair<int, int>, bool> atl;
        
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (r == 0 || c == 0) {
                    if (pac.find({r, c}) == pac.end()) {
                        pac[{r, c}] = true;
                        dfs(r, c, pac);
                    }
                } 
                
                if (r == ROWS - 1 || c == COLS - 1) {
                    if (atl.find({r, c}) == atl.end()) {
                        atl[{r, c}] = true;
                        dfs(r, c, atl);
                    }
                }
            }
        }
        vector<vector<int>> res;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (atl.find({r, c}) != atl.end() && pac.find({r, c}) != pac.end()) {
                    res.push_back({r, c});
                }
            }
        }
        return res;
    }
    
private:
    void dfs(int r, int c, map<pair<int, int>, bool>& vis) {
        for (auto d: dir) {
            int row = r + d[0];
            int col = c + d[1];
            if (row >= 0 && row < ROWS &&
                col >= 0 && col < COLS &&
                vis.find({row, col}) == vis.end() && 
                h[row][col] >= h[r][c]
               ) {
                vis[{row, col}] = true;
                dfs(row, col, vis);
            }
        }
    }
};


















