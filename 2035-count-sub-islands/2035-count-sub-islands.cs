public class Solution {
    int ROWS;
    int COLS;
    int[,] dir = {{1,0},{-1,0},{0,1},{0,-1}};
    public int CountSubIslands(int[][] grid1, int[][] grid2) {
        ROWS = grid1.Length;
        COLS = grid1[0].Length;
        bool[,] vis = new bool[ROWS,COLS];
        int res = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (!vis[r,c] && grid2[r][c] == 1) {
                    if (dfs(r, c, grid1, grid2, vis)) res++;
                }
            }
        }
        return res;
    }
    private bool dfs(int r, int c, int[][] grid1, int[][] grid2, bool[,] vis) {
        vis[r,c] = true;
        bool isSub = true;
        if (grid1[r][c] != 1) isSub = false;

        for (int i = 0; i < 4; i++) {
            int row = r + dir[i,0];
            int col = c + dir[i,1];
            if (row >= 0 && row < ROWS && 
                col >= 0 && col < COLS &&
                !vis[row,col] && grid2[row][col] == 1) {
                    if (!dfs(row, col, grid1, grid2, vis)) {
                        isSub = false;
                    }
                }
        }
        return isSub;
    }
}