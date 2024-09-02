public class Solution {
    public long ZeroFilledSubarray(int[] nums) {
        long res = 0;
        for (int i = 0; i < nums.Length; i++) {
            long increment = 1;
            while (i < nums.Length && nums[i] == 0) {
                res += increment++;
                i++;
            }
        }
        return res;

    }
}