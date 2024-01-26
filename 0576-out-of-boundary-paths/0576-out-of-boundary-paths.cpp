class Solution {
public:
    long mod = pow(10, 9) + 7;
    vector<vector<int>> directions{{1, 0},{-1, 0},{0, 1},{0, -1}};
    int m;
    int n;
    int maxMove;
    map<tuple<int, int, int>, long> cache;
    
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        this->m = m;
        this->n = n;
        this->maxMove = maxMove;
        return helper(maxMove, startRow, startColumn);
    }
    
    long helper(int steps, int row, int col) {
        if (row < 0 || row >= m || col < 0 || col >= n) {
            return 1;
        }
        if (steps == 0) return 0;
        if (cache.find({steps, row, col}) != cache.end()) return cache[{steps, row, col}];
        
        long res = 0;
        for (auto& dir: directions) {
            res = (res + helper(steps - 1, row + dir[0], col + dir[1])) % mod;
        }
        cache[{steps, row, col}] = res % mod;
        return cache[{steps, row, col}];
    }
};