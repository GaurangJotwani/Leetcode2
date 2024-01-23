#include <algorithm>

#include <algorithm>
#include <vector>
#include <string>
#include <unordered_map>

class Solution {
public:
    int maxLength(vector<string>& arr) {
        
        
        string curr;
        
        vector<int> res(1);
        res[0] = 0;
        
        helper(0, curr, arr, res);
        
        return res[0];
        
    }

private:
    void helper(int idx, string curr, vector<string>& arr,  vector<int>& res) {
        if (idx == arr.size()) {
            cout << curr;
            if (res[0] < curr.size()) {
                res[0] = curr.size();
            }
            return;
        }
        
        if (canAdd(curr, arr[idx])) {
            helper(idx + 1, curr + arr[idx], arr, res);
        }
        
        helper(idx + 1, curr, arr, res);
    }
    
    bool canAdd(string curr, string s) {
        unordered_map<char, int> seen;
        
        for (auto c: curr) {
            if (seen.find(c) != seen.end()) return false;
            seen[c]++;
        }
        
        for (auto c: s) {
            if (seen.find(c) != seen.end()) return false;
            seen[c]++;
        }
        
        return true;
    }
};