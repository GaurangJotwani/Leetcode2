public class Solution {
    public void SortColors(int[] nums) {
        int l = 0;
        int r = nums.Length - 1;
        int m = 0;
        while (m <= r) {
            Print(nums);
            if (nums[m] == 1) {
                m++;
            } else if (nums[m] == 0) {
                int tmp = nums[l];
                nums[l] = nums[m];
                nums[m] = tmp;
                l++;
                m++;
            } else {
                int tmp = nums[r];
                nums[r] = nums[m];
                nums[m] = tmp;
                r--;
            }
        }       
    }
    public void Print(int[] nums) {
        foreach(var num in nums) Console.Write(num + " ");
        Console.WriteLine();
    }
}