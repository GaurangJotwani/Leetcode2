public class Solution {
    public int[] GetSumAbsoluteDifferences(int[] nums) {
        

        var lSum = new int[nums.Length];
        var rSum = new int[nums.Length];
        if (nums.Length <= 1) return lSum;

        int n = nums.Length;
        for (int i = 1; i < n; i++) {
            lSum[i] = lSum[i - 1];
            int diff = Math.Abs(nums[i] - nums[i - 1]);
            lSum[i] += diff * i;
        }

        for (int i = n - 2; i >= 0; i--) {
            rSum[i] = rSum[i + 1];
            int diff = Math.Abs(nums[i] - nums[i + 1]);
            rSum[i] += diff * (n - i - 1);
            lSum[i] += rSum[i];
        }
        return lSum;

    }
}