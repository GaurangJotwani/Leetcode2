public class Solution {
    public bool IsPowerOfTwo(int n) {
        int numOfSetBits = 0;

        while (n != 0) {
            if ((n & 1) == 1) {
                numOfSetBits++;
                if (numOfSetBits > 1) return false;
            }
            n = n >> 1;
        }

        return numOfSetBits == 1;
    }
}