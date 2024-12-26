class Solution {
public:
    int getSum(int a, int b) {
        int num1 = a;
        int num2 = b;
        while (num2 != 0) {
            int tmp = (num1 & num2) << 1;
            num1 = num1 ^ num2;
            num2 = tmp;
        }

        return num1;
    }
};