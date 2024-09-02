public class Solution {
    public IList<int> FindDuplicates(int[] nums) {
        var res = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            int num = Math.Abs(nums[i]);
            if (nums[num - 1] < 0) res.Add(num);
            else nums[num - 1] *= -1;
        }
        return res;
    }
}