public class Solution {
    public void ReverseString(char[] s) {
        
        int l = 0;
        int r = s.Length - 1;
        while (l < r) {
            var tmp = s[l];
            s[l++] = s[r];
            s[r--] = tmp;
        }
    }
}