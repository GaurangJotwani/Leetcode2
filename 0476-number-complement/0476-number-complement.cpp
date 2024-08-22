class Solution {
public:
    int findComplement(int num) {
        int res = 0;
        int m = 0;
        while (num != 0) {
            if ((num & 1) == 0) {
                res = res | (1 << m);
            }
            m++;
            num = num / 2;
        }
        return res;
    }
};