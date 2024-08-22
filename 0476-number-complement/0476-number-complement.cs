public class Solution {
    public int FindComplement(int num) {
        int res = 0;
        int m = 0;
        while (num != 0) {
            if ((num & 1) == 0) {
                res = res | (1 << m);
            }
            num = num / 2;
            m++;
        }
        return res;

    }
}