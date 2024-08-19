class Solution {
public:
    vector<vector<string>> res;
    string s;

    void solve(int idx, vector<string> curr) {
        if (idx == s.size()) {
            res.push_back(curr);
            return;
        }

        for (int i = idx; i < s.size(); i++) {
            if (isPal(idx, i)) {
                curr.push_back(s.substr(idx, i - idx + 1));
                solve(i + 1, curr);
                curr.pop_back();
            }
        }
    }
    bool isPal(int i, int j) {
        while (i <= j) {
            if (s[i] != s[j]) return false;
            i++; j--;
        }
        return true;
    }
    vector<vector<string>> partition(string s) {
        this->s = s;
        vector<string> curr;
        solve(0, curr);
        return res;        
    }
};