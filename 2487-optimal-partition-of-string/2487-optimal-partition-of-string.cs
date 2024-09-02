public class Solution {
    public int PartitionString(string s) {
        int i = 0;
        int paritions = 0;
        while (i < s.Length) {
            var hs = new HashSet<char>();
            paritions++;
            var j = i;
            while (j < s.Length && !hs.Contains(s[j])) {
                hs.Add(s[j]);
                j++;
            }
            i = j;
        }
        return paritions;
    }
}