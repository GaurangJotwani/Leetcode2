public class Solution {
    public int[] RearrangeArray(int[] nums) {
        var n = nums.Length;
        var temp = new int[n];
        int l = 0; int r = n - 1;

        foreach(var num in nums) {
            if (num > 0) temp[l++] = num;
            else temp[r--] = num;
        }
        l = 0; r = n - 1;
        int i = 0;
        while (i < n) {
            nums[i] = temp[l++];
            nums[i + 1] = temp[r--];
            i += 2;
        }
        return nums;
    }
}