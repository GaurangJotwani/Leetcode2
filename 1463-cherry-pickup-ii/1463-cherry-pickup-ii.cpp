class Solution {
public:
    int ROWS;
    int COLS;
    vector<vector<int>> grid;
    int dp[80][80][80];
    
    int cherryPickup(vector<vector<int>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();
        this->grid = grid;
        memset(dp, -1, sizeof(dp));
        return helper(0, COLS - 1, 0);
    }
private:
    int helper(int c1, int c2, int r) {
        if (r == ROWS) return 0;
        if (dp[c1][c2][r] != -1) return dp[c1][c2][r];
        
        int ans = 0;
        for(int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                int C1 = c1 + i;
                int C2 = c2 + j;
                if (C1 >= 0 && C2 >= 0 && C1 < COLS && C2 < COLS) {
                    ans = max(ans, helper(C1, C2, r + 1));
                }
            }
        }
        if (c1 == c2) ans += grid[r][c1];
        else ans += grid[r][c1] + grid[r][c2];
        return dp[c1][c2][r] = ans;
    }
};