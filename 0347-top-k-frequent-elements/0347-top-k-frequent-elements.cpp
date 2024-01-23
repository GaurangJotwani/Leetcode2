class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>>vals(nums.size() + 1);
        unordered_map<int, int>mp;
        
        for (auto num: nums) {
            mp[num]++;
        }
        
        for (auto pair: mp) {
            vals[pair.second].push_back(pair.first);
        }
        
        
        vector<int> res;
        for (int i = vals.size() - 1; i >= 0; i--) {
            for (auto num: vals[i]) {
                res.push_back(num);
                k--;
                if (k == 0) return res;
            }
        }
        
        return res;
        
        
    }
};