public class Solution {
    public int MaxFrequency(int[] nums, int k) {
        Array.Sort(nums);  // Sort the array
        int l = 0;         // Left pointer
        long total = 0;    // Sum of elements in the current window
        int res = 0;       // Result for the maximum frequency
        
        for (int r = 0; r < nums.Length; r++) {
            total += nums[r];
            
            // Check if the current window is valid
            while ((long)nums[r] * (r - l + 1) > total + k) {
                total -= nums[l++];
            }
            
            // Update result with the size of the valid window
            res = Math.Max(res, r - l + 1);
        }
        
        return res;
    }
}
