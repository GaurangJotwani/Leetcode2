class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> curr;
        helper(curr, nums, result);
        return result;
    }

private:
    void helper(vector<int>& curr, vector<int>& nums, vector<vector<int>>& result) {
        if (nums.size() == 0) {
            result.push_back(curr);
        }

        for (int i = 0; i < nums.size(); i++) {
            curr.push_back(nums[i]);  // Add current number to current permutation

            // Remove the number from nums and call helper recursively
            int num = nums[i];
            nums.erase(nums.begin() + i);
            helper(curr, nums, result);

            // Restore the number back to nums
            nums.insert(nums.begin() + i, num);
            curr.pop_back();  // Remove last number added to current permutation
        }
    }
};