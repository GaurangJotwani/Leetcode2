public class Solution {
    public void MoveZeroes(int[] nums) {
        int l = 0, r = 0;
        while (r < nums.Length) {
            if (nums[r] != 0) {
                int tmp = nums[l];
                nums[l] = nums[r];
                nums[r] = tmp;
                l++;
            }
            r++;
        }
    }
}