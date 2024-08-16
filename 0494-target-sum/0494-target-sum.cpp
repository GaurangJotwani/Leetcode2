class Solution {
public:
    vector<int> nums;
    int target;
    map<pair<int, int>, int> dp;
    int findTargetSumWays(vector<int>& nums, int target) {
        this->nums = nums;
        this->target = target;
        return helper(0,0);
    }
private:
    int helper(int idx, int cSum) {
        if (idx == nums.size()) return cSum == target ? 1 : 0;
        if (dp.find({idx, cSum}) != dp.end()) return dp[{idx, cSum}];
        int ans = 0;
        // either add it    
        ans += helper(idx + 1, cSum + nums[idx]);
        // either subtract it
        ans += helper(idx + 1, cSum - nums[idx]);
        dp[{idx, cSum}] = ans;
        return ans;
    }
};