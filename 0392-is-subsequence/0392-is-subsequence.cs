public class Solution {
    public bool IsSubsequence(string s, string t) {
        
        if (t.Length < s.Length) return false;
        int i = 0;
        int j = 0;

        while (i < s.Length && j < t.Length) {
            if (s[i] == t[j]) {
                i++; j++;
            } else j++;
        }

        if (i == s.Length) return true;
        return false;



    }
}