class Solution {
public:
    int getSum(int a, int b) {
        int res = 0;  // Result to store the sum
        int carry = 0;  // Carry for bitwise addition
        int m = 0;  // Bit position

        while (a != 0 || b != 0 || carry != 0) {
            // Get the least significant bits of a and b
            int bit_a = a & 1;
            int bit_b = b & 1;
            
            // Calculate the sum of bits and carry
            int sum = bit_a ^ bit_b ^ carry;
            carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b));

            // Add the sum to the result
            res |= (sum << m);

            // Move to the next bit
            m++;
            a >>= 1;
            b >>= 1;
            if (m >= 32) break;
        }

        return res;
    }
};