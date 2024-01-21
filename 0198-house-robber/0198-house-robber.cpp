class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return max(nums[0], nums[1]);
        
        int first = nums[0];
        int second = max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.size(); i++) {
            int temp = second;
            second = max(nums[i] + first, second);
            first = temp;
        }
        
        return second;
    }
};