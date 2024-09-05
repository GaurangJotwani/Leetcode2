public class Solution {
    public int MinOperations(int[] nums, int x) {
        int total = 0;
        foreach (var num in nums) total += num;
        int target  = total - x, window = -1, sum = 0, l = 0, n = nums.Length;

        for (int r = 0; r < n; r++) {
            sum += nums[r];

            while (l <= r && sum > target) sum -= nums[l++];

            if (sum == target) window = Math.Max(window, r - l + 1);
        }

        return window == - 1 ? -1 : n - window; 




    }
}