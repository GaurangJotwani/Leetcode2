public class Solution {
    public int DeleteAndEarn(int[] nums) {
        
        var counts = new Dictionary<int, int>();
        foreach(var num in nums) counts[num] = counts.ContainsKey(num) ? counts[num] + 1 : 1;
        
        nums = nums.ToHashSet().ToArray();
        Array.Sort(nums);

        var dp = new int[nums.Length + 1];
        dp[1] = counts[nums[0]] * nums[0];

        for (int i = 2; i < dp.Length; i++) {
            if (nums[i - 2] + 1 != nums[i - 1]) dp[i] = dp[i - 1] + counts[nums[i - 1]] * nums[i - 1];
            else dp[i] = Math.Max(dp[i - 1], dp[i - 2] + counts[nums[i - 1]] * nums[i - 1]);
        }

        return dp[nums.Length];
        

    }
}