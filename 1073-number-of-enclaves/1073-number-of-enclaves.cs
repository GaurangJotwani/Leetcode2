public class Solution {
    int[,] dir = new int[,] {{1,0},{-1,0},{0,1},{0,-1}};
    int ROWS;
    int COLS;

    public int NumEnclaves(int[][] grid) {
        ROWS = grid.Length;
        COLS = grid[0].Length;
        var vis = new bool[ROWS,COLS];

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (r == 0 || c == 0 || r == ROWS - 1 || c == COLS - 1) {
                    if (!vis[r,c] && grid[r][c] == 1) dfs(r, c, vis, grid);
                }
            }
        }

        int res = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) res++;
            }
        }
        return res;
    }

    public void dfs(int r, int c, bool[,] vis, int[][] grid) {
        vis[r,c] = true;
        grid[r][c] = -1;
        for (int i = 0; i < 4; i++) {
            int row = r + dir[i,0], col = c + dir[i,1];
            if (row >= 0 && row < ROWS && col >= 0 && col < COLS && !vis[row,col] && grid[row][col] == 1) {
                dfs(row, col, vis, grid);
            }
        }
    }
}