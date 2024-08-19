class Solution {
public:
    vector<vector<string>> res;
    unordered_set<int> cols;
    unordered_set<int> pos_diag;
    unordered_set<int> neg_diag;
    int n;
    vector<vector<string>> solveNQueens(int n) {
        vector<string> start;
        this->n = n;
        for (int i = 0; i < n; i++) {
            string s = "";
            for (int i = 0; i < n; i++) {
                s.push_back('.');
            }
            start.push_back(s);
        }        
        
        solve(0, start);
        return res;
    }

    void solve(int r, vector<string> &start) {
        if (r == n) {
            res.push_back(start);
            return;
        }
        for (int c = 0; c < n; c++) {
            if (cols.find(c) != cols.end()) continue;
            if (neg_diag.find(r + c) != neg_diag.end()) continue;
            if (pos_diag.find(c - r) != pos_diag.end()) continue;
            
            start[r][c] = 'Q';
            cols.insert(c);
            neg_diag.insert(r + c);
            pos_diag.insert(c - r);
            solve(r + 1, start);
            start[r][c] = '.';
            cols.erase(c);
            neg_diag.erase(r + c);
            pos_diag.erase(c - r);
        }
    }
};