class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> m;
        for (auto s: strs) m[getKey(s)].push_back(s);
        vector<vector<string>> res;
        for (auto pair: m) res.push_back(pair.second);
        return res;
    }

private:
    string getKey(string s) {
        vector<int> counts(26);
        for (auto c: s) counts[c - 'a']++;
        string key = "";
        for (auto c: counts) key += to_string(c) + "#";
        return key;
    }
};