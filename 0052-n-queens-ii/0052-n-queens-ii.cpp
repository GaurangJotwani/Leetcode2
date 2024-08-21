class Solution {
public:
    int res;
    unordered_set<int> cols;
    unordered_set<int> pos_diag;
    unordered_set<int> neg_diag;
    int n;
    int totalNQueens(int n) {
        res = 0;
        this->n = n;
        solve(0);
        return res;
    }

    void solve(int r) {
        if (r == n) {
            res++;
            return;
        }
        for (int c = 0; c < n; c++) {
            if (cols.find(c) != cols.end()) continue;
            if (neg_diag.find(r + c) != neg_diag.end()) continue;
            if (pos_diag.find(c - r) != pos_diag.end()) continue;  
            cols.insert(c);
            neg_diag.insert(r + c);
            pos_diag.insert(c - r);
            solve(r + 1);
            cols.erase(c);
            neg_diag.erase(r + c);
            pos_diag.erase(c - r);
        }
    }
};