class Solution {
public:
    vector<vector<int>> res;
    int target;
    vector<int> nums;

    void dp(vector<int> curr, int i, int cSum) {
        if (cSum == target) {
            res.push_back(curr);
            return;
        }
        if (i >= nums.size()) return;
        // include
        if (nums[i] + cSum <= target) {
            curr.push_back(nums[i]);
            dp(curr, i, cSum + nums[i]);
            curr.pop_back();
        }
        //exclude
        dp(curr, i + 1, cSum);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> curr;
        this->target = target;
        nums = candidates;
        dp(curr, 0, 0);
        return res;
    }
};