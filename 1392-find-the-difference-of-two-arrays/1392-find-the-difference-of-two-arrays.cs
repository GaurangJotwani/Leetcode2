public class Solution {
    public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) {
        var hashSet1 = new HashSet<int>(nums1);
        var hashSet2 = new HashSet<int>(nums2);

        var res = new IList<int>[2];
        res[0] = new List<int>();
        res[1] = new List<int>();

        foreach (var num in hashSet1) {
            if (!hashSet2.Contains(num)) res[0].Add(num);
        }

        foreach (var num in hashSet2) {
            if (!hashSet1.Contains(num)) res[1].Add(num);
        }

        return res;
    }
}