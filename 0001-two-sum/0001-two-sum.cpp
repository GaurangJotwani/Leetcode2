class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> s;
        for (int i = 0; i < nums.size(); i++) s[nums[i]] = i;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (s.find(diff) != s.end() && s[diff] != i) {
                return {i, s[diff]};
            } 
            
        }
        return {};

    }
};