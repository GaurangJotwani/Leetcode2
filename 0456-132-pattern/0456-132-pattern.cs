public class Solution {
    public bool Find132pattern(int[] nums) {
        var stk = new Stack<(int num, int min)>();
        int n = nums.Length, curMin = nums[0];

        for (int i = 1; i < n; i++) {
            int num = nums[i];

            while (stk.Count > 0 && num >= stk.Peek().num) stk.Pop();
            if (stk.Count > 0 && num > stk.Peek().min) return true;

            stk.Push((num, curMin));
            curMin = Math.Min(curMin, num);
        }


        return false;
    }
}