public class Solution {
    public int[] NextGreaterElement(int[] nums1, int[] nums2) {
        var stk = new Stack<int>();
        var mp = new Dictionary<int, int>();
        int[] res2 = new int[nums1.Length];

        for (int i = 0; i < nums2.Length; i++) {
            var num = nums2[i];
            while (stk.Count != 0 && stk.Peek() < num) {
                var top = stk.Peek();
                mp[top] = num;
                stk.Pop();
            }
            stk.Push(num);
        }

        int[] res = new int[nums1.Length];
        for(int i = 0; i < nums1.Length; i++) {
            var num = nums1[i];
            if (mp.ContainsKey(num)) res[i] = mp[num];
            else res[i] = -1;
        }
        return res;
    }
}