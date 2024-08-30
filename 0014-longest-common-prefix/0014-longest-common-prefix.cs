public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        var res = new StringBuilder("");
        int minLength = int.MaxValue;
        if (strs.Length == 1) return strs[0];

        int j = 1;
        while (true) {
            for(int i = 1; i < strs.Length; i++) {
                if (strs[i - 1].Length == 0 ||  strs[i].Length == 0) return "";
                if (strs[i].Length == j - 1 || strs[i - 1].Length == j - 1) return res.ToString();
                if (strs[i].Substring(0, j) != strs[i - 1].Substring(0, j)) return res.ToString();
            }
            res.Append(strs[0][j - 1]);
            j++;
        }
        return res.ToString();
    }
}