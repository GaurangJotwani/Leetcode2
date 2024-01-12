class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int n = nums.size();
        unordered_map<int, int> mp;
        
        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (mp.find(complement) != mp.end()) {
                vector<int> v;
                v.push_back(mp[complement]);
                v.push_back(i);
                return v;
            }
            
            mp.insert({nums[i], i});
        }
        
        return {};
    }
};