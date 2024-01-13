class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int n = nums.size();
        int curMin = 1, curMax = 1;
        for (int i = 0; i < n; i++) {
            
            int num = nums[i];
            int tmp = curMax * num;
            curMax = max(max(curMin * num, curMax * num), num);
            curMin = min(min(curMin * num, tmp), num);
            res = max(res, curMax);
        }
        
        return res;
    }
};