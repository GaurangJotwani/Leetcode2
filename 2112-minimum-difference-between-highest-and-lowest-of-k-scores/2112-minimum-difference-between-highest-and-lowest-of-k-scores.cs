public class Solution {
    public int MinimumDifference(int[] nums, int k) {
        int n = nums.Length;
        Array.Sort(nums);
        int l = 0, minDiff = int.MaxValue;
        for (int r = 0; r < n; r++) {
            if (r - l + 1 == k) {
                minDiff = Math.Min(minDiff, nums[r] - nums[l]);
                l++;
            }
        }
        return minDiff;
    }
}