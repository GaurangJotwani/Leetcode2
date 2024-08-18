class Solution {
public:
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        this->nums = nums;
        vector<int> curr;
        solve(curr, 0);
        return res;
    }
private:
    vector<vector<int>> res;
    vector<int> nums;
    void solve(vector<int> &curr, int idx) {
        if(idx == nums.size()) {
            res.push_back(curr);
            return;
        }
        // include
        curr.push_back(nums[idx]);
        solve(curr, idx + 1);
        curr.pop_back();
        // exclude
        idx++;
        while (idx < nums.size() && nums[idx] == nums[idx - 1]) idx++;
        solve(curr, idx);
    }

};