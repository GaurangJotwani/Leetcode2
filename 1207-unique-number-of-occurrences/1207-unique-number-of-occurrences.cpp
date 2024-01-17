class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
        unordered_map<int, int> mp;
        for (auto num: arr) {
            mp[num]++;
        }
        
        unordered_map<int,bool> mp2;
        
        for (auto pair: mp) {
            if (mp2.find(pair.second) != mp2.end()) return false;
            mp2[pair.second] = true;
        }
        
        return true;
        
    }
};