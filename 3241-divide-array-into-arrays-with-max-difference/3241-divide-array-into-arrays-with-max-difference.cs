public class Solution {
    public int[][] DivideArray(int[] nums, int k) {
        
        int n = nums.Length;
        var res = new List<int[]>();
        Array.Sort(nums);
        int i = 0;

        var tmp = new List<int>();

        while (i < n) {
            int anchor = nums[i++];
            tmp.Add(anchor);
            while (i < nums.Length && nums[i] - anchor <= k && tmp.Count < 3) {
                tmp.Add(nums[i++]);
            } 
            res.Add(tmp.ToArray());
            tmp = new List<int>();
            if (res.Count > n / 3) return new int[0][];
        }
        return res.ToArray();
    }
}