class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> curr;
        sort(candidates.begin(), candidates.end());
        helper(0, curr, 0, result, candidates, target);
        return result;
    }
private:
    void helper(int idx, vector<int>& curr, int cSum, vector<vector<int>>& result, vector<int>& candidates, int target) {
        
        if (cSum == target) {
            result.push_back(curr);
            return;
        }
        
        if (idx == candidates.size()) return;
        if (cSum > target) return;
        
        curr.push_back(candidates[idx]);
        helper(idx + 1, curr, cSum + candidates[idx], result, candidates, target);
        curr.pop_back();
        idx += 1;
        while (idx < candidates.size() && candidates[idx - 1] == candidates[idx]) {
            idx++;
        }
        helper(idx, curr, cSum, result, candidates, target);
    }
};