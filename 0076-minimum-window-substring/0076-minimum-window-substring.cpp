class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> s_d;
        unordered_map<char, int> t_d;
        if (s.size() < t.size()) return "";
                
        for (auto c: t) {
            t_d[c]++;
        }
        
        int l = 0;
        int r = 0;
        int res = INT_MAX;
        pair<int, int> p;
        
        while (r < s.size()) {
            s_d[s[r]]++;
            if (areMatching(s_d, t_d)) {
                if (r - l + 1 < res) {
                    res = r - l + 1;
                    p.first = l;
                    p.second = r;
                }
                s_d[s[l]]--;
                if (s_d[s[l]] == 0) {
                    s_d.erase(s[l]);
                }
                l++;
                while (l <= r && areMatching(s_d, t_d)) {
                        if (r - l + 1 < res) {
                            res = r - l + 1;
                            p.first = l;
                            p.second = r;
                        }
                        s_d[s[l]]--;
                        if (s_d[s[l]] == 0) {
                            s_d.erase(s[l]);
                        } 
                        l++;
                    }
            }
            r++;
        }
        cout << p.second;
        if (res == INT_MAX) return "";
        return s.substr(p.first, p.second - p.first + 1);
        
    }
private:
    bool areMatching(const unordered_map<char, int>& s, const unordered_map<char, int>& t) {
    for (const auto& p : t) {
        auto s_iter = s.find(p.first);
        if (s_iter == s.end() || p.second > s_iter->second) {
            return false;
        }
    }
    return true;
}
};