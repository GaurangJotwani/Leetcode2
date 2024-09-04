public class Solution {
    public long LargestPerimeter(int[] nums) {
        long res = -1;
        int n = nums.Length;
        if (n <= 2) return -1;
        
        Array.Sort(nums);
        long[] prefix = new long[n];
        prefix[0] = nums[0];

        for (int i = 1; i < n; i++) prefix[i] += prefix[i - 1] + nums[i];

        for (int i = 2; i < n; i++) {
            if (nums[i] < prefix[i - 1]) {
                res = Math.Max(res, prefix[i - 1] + nums[i]);
            }
        }
        return res;
    }
}