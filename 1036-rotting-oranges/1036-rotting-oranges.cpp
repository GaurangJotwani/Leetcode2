class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        
        int ROWS = grid.size();
    int COLS = grid[0].size();
    vector<vector<int>> dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));
    std::queue<pair<int, int>> Q;
    
    // Push all initial rotten oranges into the queue
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (grid[i][j] == 2) {
                visited[i][j] = true;
                Q.push({i, j});
            }
        }
    }
    
    int t = 0;
    while (!Q.empty()) {
        int s = Q.size();
        bool newRotten = false; // Flag to check if any new oranges are rotted in this level
        for (int i = 0; i < s; i++) {
            int r = Q.front().first;
            int c = Q.front().second;
            Q.pop();
            for (auto d : dir) {
                int row = r + d[0];
                int col = c + d[1];
                if (row >= 0 && row < ROWS && col >= 0 && col < COLS && !visited[row][col] && grid[row][col] == 1) {
                    grid[row][col] = 2;
                    Q.push({row, col});
                    visited[row][col] = true;
                    newRotten = true; // Set the flag as new oranges are rotted
                }
            }
        }
        if (newRotten) {
            t++; // Increment time only if new oranges are rotted
        }
    }
    
    // Check if there are any fresh oranges left
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (grid[i][j] == 1) {
                return -1; // If any fresh orange is found, return -1
            }
        }
    }
    
    return t;
    }
};


// ROWS, COLS = len(grid), len(grid[0])
//         q = deque()
//         time = -1
//         seen = set()
//         directions = [(0,1), (0,-1), (1,0), (-1,0)]
//         fresh_orange_found = False
        
//         for r in range(ROWS):
//             for c in range(COLS):
//                 if grid[r][c] == 2:
//                     seen.add((r, c))
//                     q.append((r, c))
//                 elif grid[r][c] == 1:
//                     fresh_orange_found = True
        
//         if not fresh_orange_found:
//             return 0
        
//         while q:
//             for i in range(len(q)):
//                 r, c = q.popleft()
//                 for dr, dc in directions:
//                     row, col = r + dr, c + dc
//                     if (0 <= row < ROWS and
//                         0 <= col < COLS and
//                         (row, col) not in seen and
//                         grid[row][col] == 1
//                        ):
//                         grid[row][col] = 2
//                         seen.add((row, col))
//                         q.append((row, col))
//             time += 1
                        
        
//         # print(grid, time)
//         for r in range(ROWS):
//             for c in range(COLS):
//                 if grid[r][c] == 1:
//                     return -1
//         return time