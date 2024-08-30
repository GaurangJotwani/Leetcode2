public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        var res = new StringBuilder("");
        int minLength = int.MaxValue;
        foreach(var word in strs) minLength = Math.Min(word.Length, minLength);
        if (minLength == 0) return "";
        if (strs.Length == 1) return strs[0];

        for (int j = 1; j <= minLength; j++) {
            for(int i = 1; i < strs.Length; i++) {
                if (strs[i].Substring(0, j) != strs[i - 1].Substring(0, j)) return res.ToString();
            }
            res.Append(strs[0][j - 1]);
        }

        return res.ToString();
    }
}