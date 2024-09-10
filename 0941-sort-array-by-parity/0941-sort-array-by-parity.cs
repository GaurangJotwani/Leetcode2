public class Solution {
    public int[] SortArrayByParity(int[] nums) {
        int l = 0, n = nums.Length;
        int r = n - 1;
        while (l < r) {
            while (l < r && nums[l] % 2 == 0) l++;

            while (l < r && nums[r] % 2 == 1) r--;

            int tmp = nums[r];
            nums[r] = nums[l];
            nums[l] = tmp;
        }

        return nums;
    }
}