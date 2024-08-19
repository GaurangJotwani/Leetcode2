class Solution {
public:
    double solve(double x, int n) {
        
        double res = 1;
        while (n != 0) {
            if (n & 1) res = res * x;
            x = x * x;
            n = n >> 1;
        }
        return res;
    }

    double myPow(double x, int n) {
        if (n == 0) return 1;
        double ans = solve(x, abs(n));
        if (n > 0) return ans;
        else return 1/ans;
    }
};