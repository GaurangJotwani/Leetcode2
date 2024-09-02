public class Solution {
    public int FindMaxLength(int[] nums) {
        int res = 0;
        int prefix = 0;
        var hm = new Dictionary<int, int>{{0,-1}};
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 0) prefix--;
            else prefix++;
            if (hm.ContainsKey(prefix)) {
                res = Math.Max(i - hm[prefix], res);
            } else hm[prefix] = i;
        }
        return res;
    }
}