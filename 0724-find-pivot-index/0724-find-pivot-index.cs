public class Solution {
    public int PivotIndex(int[] nums) {
        var leftSum = new int[nums.Length];
        var rightSum = new int[nums.Length];
        int curr = 0;
        for (int i = nums.Length - 1; i >= 0; i--) {
            rightSum[i] = curr;
            curr += nums[i];
        }
        curr = 0;
        for (int i = 0; i < nums.Length; i++) {
            leftSum[i] = curr;
            if (leftSum[i] == rightSum[i]) return i;
            curr += nums[i];
        }
        return -1;

    }
}