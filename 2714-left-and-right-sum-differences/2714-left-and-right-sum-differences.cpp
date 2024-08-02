class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int totalSum = 0;
        for (auto num: nums) {
            totalSum += num;
        }
        int cSum = 0;
        for (int i = 0; i < nums.size(); i++) {
            int temp = abs(cSum - (totalSum - cSum - nums[i])); 
            cSum += nums[i];
            nums[i] = temp;
        }
        return nums;
    }
};