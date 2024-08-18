class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        this->target = target;
        sort(candidates.begin(), candidates.end());
        this->nums = candidates;
        vector<int> curr;
        knapsack(0, 0, curr);
        return res;
    }
private:
int target;
vector<int> nums;
vector<vector<int>> res;
void knapsack(int idx, int cSum, vector<int> &curr) {
    if (cSum == target) {
        res.push_back(curr);
        return;
    }
    if (idx == nums.size()) return;

    // include in answer
    if (cSum + nums[idx] <= target) {
        curr.push_back(nums[idx]);
        knapsack(idx + 1, cSum + nums[idx], curr);
        curr.pop_back();
    }
    // exclude in answer
    idx++;
    while (idx < nums.size() && nums[idx] == nums[idx - 1])idx++;
    knapsack(idx, cSum, curr);
}

};