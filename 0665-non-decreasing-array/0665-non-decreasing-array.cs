public class Solution {
    public bool CheckPossibility(int[] nums) {
        
        int n = nums.Length;
        var changes = 0;
        if (n == 1) return true;

        for (int i = 0; i < n - 1; i++) {
            if (i == 0) {
                if (nums[i + 1] < nums[i]) {
                    changes++;
                    if (changes == 2) return false;
                    nums[i] = nums[i + 1];
                }
            } else if (nums[i + 1] < nums[i]) {
                changes++;
                if (changes == 2) return false;
                if (nums[i + 1] < nums[i - 1]) nums[i + 1] = nums[i];
                else nums[i] = nums[i - 1];
            }
        }
        return true;
    }
}