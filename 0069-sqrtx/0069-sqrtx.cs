public class Solution {
    public int MySqrt(int x) {
        int i = 1;
        while (i <= x / i) i++;
        return i - 1;
    }
}