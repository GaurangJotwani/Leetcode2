class Solution {
public:
vector<int> nums;
int n;
    int rob(vector<int>& nums) {
        this->nums = nums;
        n = nums.size();
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return max(nums[0], nums[1]);

        int f = helper(0, nums.size() - 2);
        int s = helper(1, nums.size() - 1);
        return max(f, s);   
    }
private:
    int helper(int start, int end) {
        int first = 0;
        int second = nums[start];
        for (int i = start + 1; i <= end; i++) {
            int temp_max = max(second, first + nums[i]);
            first = second;
            second = temp_max;
        }
        return second;
    }
};