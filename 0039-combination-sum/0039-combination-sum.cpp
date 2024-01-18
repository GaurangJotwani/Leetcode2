class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> curr;
        int cSum = 0;
        helper(0, cSum, curr, candidates, target, result);
        return result;
    }
private:
    void helper(int idx, int cSum, vector<int>&curr, vector<int>& candidates, int target, vector<vector<int>>& result) {
        if (cSum == target) {
            result.push_back(curr);
            return;
        }
        
        if (idx == candidates.size()) return;
        if (cSum > target) return;
        
        curr.push_back(candidates[idx]);
        helper(idx, cSum + candidates[idx], curr, candidates, target, result);
        curr.pop_back();
        
        helper(idx + 1, cSum, curr, candidates, target, result);
        
        
    }
    
    
};