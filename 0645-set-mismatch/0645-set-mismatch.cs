public class Solution {
    public int[] FindErrorNums(int[] nums) {
        int n = nums.Length;
        var s = new HashSet<int>();
        var res = new int[2];

        for (int i = 0; i < n; i++) {
            if (s.Contains(nums[i])) {
                res[0] = nums[i];
                continue;
            }
            s.Add(nums[i]);
        }

        for (int i = 1; i <= n; i++) {
            if (!s.Contains(i)) {
                res[1] = i;
                break;
            }
        }

        return res;
    }
}