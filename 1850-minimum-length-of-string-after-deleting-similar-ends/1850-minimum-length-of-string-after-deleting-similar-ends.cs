public class Solution {
    public int MinimumLength(string s) {
        int n = s.Length;
        var l = 0;
        var r = n - 1;

        while (l < r) {
            if (s[l] != s[r]) return r - l + 1;
            l++;
            while (l < r && s[l] == s[l - 1]) l++;
            if (l == r) return 0;
            r--;
            while (r > l && s[r] == s[r + 1]) r--; 
        }

        return 1;
    }
}