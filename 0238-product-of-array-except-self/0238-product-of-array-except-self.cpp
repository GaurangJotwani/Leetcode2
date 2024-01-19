class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>left;
        vector<int>right(nums.size());
        
        int r = 1;
        for (int i = 0; i < nums.size(); i++) {
           left.push_back(r);
            r *= nums[i];
        }
        
        r = 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            right[i] = r;
            r *= nums[i];
        }
        
        
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            res.push_back(left[i] * right[i]);
        }
        
        return res;
    }
};