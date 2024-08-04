class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> left(nums.size());
        vector<int> right(nums.size());
        vector<int> res(nums.size());

        int ans = 1;
        for (int i = 0; i < nums.size(); i++) {
            left[i] = ans;
            ans *= nums[i];
        }
        ans = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            right[i] = ans;
            res[i] = left[i] * right[i];
            ans *= nums[i];
        }
        return res;
    }
};