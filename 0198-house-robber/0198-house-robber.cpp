class Solution {
public:
    int rob(vector<int>& nums) {
        
        if (nums.size() == 1) return nums[0];
        int first = 0;
        int second = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            int res = max(nums[i] + first, second);
            cout << res << "\n";
            first = second;
            second = res;
        }

        return second;
    }
};