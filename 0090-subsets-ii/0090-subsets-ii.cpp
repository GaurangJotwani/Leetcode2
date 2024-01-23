class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> curr;
        sort(nums.begin(), nums.end());
        helper(0, curr, nums, result);
        return result;
    }
private:
    void helper(int idx, vector<int>& curr, vector<int>& nums,  vector<vector<int>>& result) {
        
        if (idx == nums.size()) {
            result.push_back(curr);
            return;
        }
        curr.push_back(nums[idx]);
        helper(idx + 1, curr, nums, result);
        curr.pop_back();
        idx++;
        while (idx < nums.size() && nums[idx] == nums[idx - 1]) {
            idx++;
        }
        helper(idx, curr, nums, result);
    }
};