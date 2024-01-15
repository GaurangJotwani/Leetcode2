class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for (int i = 0; i < strs.size(); i++) {
            m[getKey(strs[i])].push_back(strs[i]);
        }
        
        vector<vector<string>> res;
        for (auto pair: m) {
            res.push_back(pair.second);
        }
        
        return res;
    }
private:
    string getKey(string s) {
        vector<int> count(26);
        
        for (auto c: s) {
            count[c - 'a']++;
        }
        
        string key = "";
        for (auto i: count) {
            key = key + to_string(i) + '#';
        }
        return key;
    }
};