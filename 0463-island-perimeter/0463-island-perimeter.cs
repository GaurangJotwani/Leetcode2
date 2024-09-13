public class Solution {
    private int[][] dir = new int[][] {[1,0],[-1,0],[0,1],[0,-1]};
    private int ROWS;
    private int COLS;

    public int IslandPerimeter(int[][] grid) {
        ROWS = grid.Length;
        COLS = grid[0].Length;
        var visited = new bool[ROWS, COLS];

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1) return dfs(r, c, grid, visited);
            }
        }
        return 0;
    }

    private int dfs(int r, int c, int[][] grid, bool[,] visited) {
        visited[r,c] = true;
        int ans = 0;
        foreach (var d in dir) {
            int row = r + d[0];
            int col = c + d[1];
            if (row >= 0 && row < ROWS && 
                col >= 0 && col < COLS && 
                grid[row][col] == 1)
            {
                if (!visited[row,col]) ans += dfs(row, col, grid, visited);
            } 
            else ans++;
        }
        return ans;
    } 
}