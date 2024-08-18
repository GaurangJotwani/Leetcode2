class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int res = 0;
        for (int i = 31; i >= 0; i--) {
            int mask = 1 << i;
            if (n & mask) {
                res = res | (1 << (31 - i));
            }
        }
        return res;
    }
};