public class Solution {
    public int MaxProductDifference(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int big = nums[n - 1] * nums[n - 2];
        int small = nums[0] * nums[1];

        return big - small;
    }
}