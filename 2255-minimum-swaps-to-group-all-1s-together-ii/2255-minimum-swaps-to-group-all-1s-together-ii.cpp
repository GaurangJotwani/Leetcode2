class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int totalOnes = 0;
        for (auto num: nums) totalOnes += num;

        int maxWindow = 0;
        int cWindow = 0;

        for (int i = 0; i < totalOnes; i++) {
            cWindow += nums[i];
        }
        maxWindow = cWindow;
        
        for (int start = 1; start < nums.size(); start++) {
            cWindow -= nums[start - 1];
            cWindow += nums[(start + totalOnes - 1) % nums.size()];
            maxWindow = max(maxWindow, cWindow);
        }

        return totalOnes - maxWindow;


    }
};