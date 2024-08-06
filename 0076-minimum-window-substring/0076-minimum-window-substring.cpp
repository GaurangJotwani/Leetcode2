class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> freq_s;
        unordered_map<char, int> freq_t;
        if (s.size() < t.size()) return "";

        for (auto c: t) freq_t[c]++;
        int res = INT_MAX, r = 0, l = 0;
        pair<int, int> indices;

        while (r < s.size()) {
            freq_s[s[r]]++;
            while (l <= r && areMatching(freq_s, freq_t)) {
                if (r - l + 1 < res) {
                    res = r - l + 1;
                    indices = {l, r};
                }
                freq_s[s[l]]--;
                if (freq_s[s[l]] == 0) freq_s.erase(s[l]);
                l++;
            }
            r++;
        }
        if (res == INT_MAX) return "";
        return s.substr(indices.first, indices.second - indices.first + 1);
    }

private:
    bool areMatching(unordered_map<char, int> &freq_s, unordered_map<char, int> &freq_t) {
        for (auto c: freq_t) {
            if (freq_s.find(c.first) == freq_s.end()) return false;
            if (freq_s[c.first] < c.second) return false;
        }
        return true;
    }
};