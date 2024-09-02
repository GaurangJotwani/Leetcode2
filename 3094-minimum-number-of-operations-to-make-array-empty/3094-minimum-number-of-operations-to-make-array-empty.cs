public class Solution {
    public int MinOperations(int[] nums) {
        int[] dp = new int[nums.Length + 1];
        if (nums.Length == 1) return -1;
        int res = 0;
        dp[0] = 0;
        dp[1] = int.MaxValue;
        for (int i = 2; i <= nums.Length; i++) {
            int ans1 = i - 3 >= 0 ? dp[i - 3] : int.MaxValue;
            int ans2 = dp[i - 2];
            dp[i] = 1 + Math.Min(ans1, ans2);
        }

        var counts = new Dictionary<int, int>();
        foreach(var num in nums) {
            if (counts.ContainsKey(num)) counts[num]++;
            else counts[num] = 1;
        } 

        foreach (var kvp in counts) {
            if (kvp.Value == 1) return -1;
            res += dp[kvp.Value];
        }
        return res;
    }
}