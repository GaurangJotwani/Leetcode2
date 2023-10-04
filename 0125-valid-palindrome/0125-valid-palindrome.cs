public class Solution {
    public bool IsPalindrome(string s) {
        
        StringBuilder stringBuilder = new StringBuilder();
        
        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            if (char.IsLetter(c)) {
                stringBuilder.Append(char.ToLower(c));
            } else if (char.IsDigit(c)) {
                stringBuilder.Append(char.ToLower(c));
            }
        }
        
        string s_copy = stringBuilder.ToString();
        int left = 0;
        int right = s_copy.Length - 1;
        while (left < right) {
            if (s_copy[left] != s_copy[right]) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        
        
        return true;
    }
}