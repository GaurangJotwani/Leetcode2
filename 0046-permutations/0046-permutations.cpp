class Solution {
public:
    vector<vector<int>> res;
    vector<int> nums;
    void permute(vector<int> &curr, vector<int> remain) {
        if (curr.size() == nums.size()) {
            res.push_back(curr);
            return;
        }
        for (int i = 0; i < remain.size(); i++) {
            curr.push_back(remain[i]);
            vector<int> temp;
            for (int j = 0; j < i; j++) temp.push_back(remain[j]);
            for (int j = i + 1; j < remain.size(); j++) temp.push_back(remain[j]);
            permute(curr, temp);
            curr.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        this->nums = nums;
        vector<int> curr;
        permute(curr, nums);
        return res;
    }
};