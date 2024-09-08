public class Solution {
    public string FirstPalindrome(string[] words) {
        foreach (var word in words) if (IsPalindrome(word)) return word;
        return "";
    }

    public bool IsPalindrome(string s) {
        int l = 0, r = s.Length - 1;
        while (l < r) if (s[l++] != s[r--]) return false;
        return true;
    }
}