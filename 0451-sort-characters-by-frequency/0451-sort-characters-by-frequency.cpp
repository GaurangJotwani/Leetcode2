class Solution {
public:
    string frequencySort(string s) {
        
        unordered_map<char, int> mp;
        for (auto c : s) {
            mp[c]++;
        }
        
        vector<vector<char>> freq(s.size() + 1);
        
        for (auto pair: mp) {
            freq[pair.second].push_back(pair.first);
        }
        
        vector<char> res;
        for (int i = freq.size() - 1; i >= 0; i--) {
            for (auto c: freq[i]) {
                for (int j = 0; j < i; j++) {
                    res.push_back(c);
                }
            }
        }
        
        
        
        
        
        string temp(res.begin(), res.end());
        return temp;
    }
};