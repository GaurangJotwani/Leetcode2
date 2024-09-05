public class Solution {
    public int NumSubarraysWithSum(int[] nums, int goal) {
        
        return helper(nums, goal) - helper(nums, goal - 1);
    }

    private int helper(int[] nums, int x) {
        if (x < 0) return 0;
        int l = 0, res = 0, n = nums.Length, sum = 0;

        for (int r = 0; r < n; r++) {
            sum += nums[r];
            while (sum > x) sum -= nums[l++];
            res += (r - l + 1);
        }

        return res;

    }
}