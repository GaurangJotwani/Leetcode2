public class Solution {
    public int MaxSumMinProduct(int[] nums) {
        long mod = 1000000007;
        int n = nums.Length;
        long[] ps = new long[n + 1]; // prefix sum array
        Stack<int> stack = new Stack<int>();
        stack.Push(-1);
        long res = 0;

        // Compute the prefix sum
        for (int i = 0; i < n; i++)
        {
            ps[i + 1] = ps[i] + nums[i];
        }

        Array.Resize(ref nums, n + 1);
        nums[n] = 0;

        for (int i = 0; i <= n; i++)
        {
            while (stack.Peek() != -1 && nums[stack.Peek()] > nums[i])
            {
                int minIndex = stack.Pop();
                long minVal = nums[minIndex];
                int leftIndex = stack.Peek();
                long rangeSum = ps[i] - ps[leftIndex + 1]; // prefix sum difference
                res = Math.Max(res, rangeSum * minVal);
            }
            stack.Push(i);
        }

        return (int)(res % mod);
    }
}
