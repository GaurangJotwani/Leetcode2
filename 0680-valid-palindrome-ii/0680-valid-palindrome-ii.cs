public class Solution {
    public bool ValidPalindrome(string s) {
        int l = 0;
        int r = s.Length - 1;

        while (l < r) {
            if (s[l] != s[r]) {
                if (IsPalindrome(s.Substring(l, r - l)) || IsPalindrome(s.Substring(l + 1, r - l))) return true;
                else return false;                
            }
            l++; r--;
        }

        return true;
    }

    private bool IsPalindrome(string s) {
        int l = 0, r = s.Length - 1;
        while (l < r) if (s[l++] != s[r--]) return false;
        return true;

    }
}