public class Solution {
    public int[] Intersection(int[] nums1, int[] nums2) {
        var st = new HashSet<int>();
        foreach(var num in nums1) st.Add(num);

        var tmp = new HashSet<int>();
        foreach (var num in nums2) if (st.Contains(num))tmp.Add(num);

        var res = new int[tmp.Count];
        var i = 0;
        foreach(var num in tmp) res[i++]=num;

        return res;





    }
}