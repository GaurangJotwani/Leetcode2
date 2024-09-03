public class Solution {
    public int NumSubseq(int[] nums, int target) {
        Array.Sort(nums);

        // Initialize variables
        int mod = 1000000007;
        int n = nums.Length;
        int ans = 0;

        // Calculate powers of 2 modulo mod
        int[] pow2 = new int[n];
        pow2[0] = 1;
        for (int i = 1; i < n; i++) {
            pow2[i] = (pow2[i - 1] * 2) % mod;
        }

        // Use two pointers to find subsequences
        int left = 0, right = n - 1;
        while (left <= right) {
            if (nums[left] + nums[right] > target) {
                right--; // Move the right pointer left if the sum is too large
            } else {
                // Add the number of valid subsequences starting from 'left'
                ans = (ans + pow2[right - left]) % mod;
                left++; // Move the left pointer to the right
            }
        }

        return ans;

    }
}