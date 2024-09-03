public class Solution {
    public int[] RearrangeArray(int[] nums) {
        int n = nums.Length;
        if (n == 1) return nums;
        Array.Sort(nums);
        var res = new int[n];

        int l = 0;
        int r = nums.Length - 1;
        int i = 0;

        while (l <= r) {
            res[i] = nums[l++];
            if (i + 1 < n) res[i + 1] = nums[r--];
            i+=2;
        }
        return res;
    }
}