public class Solution {
    public int ArrangeCoins(int n) {
        long sum = 0;
        int i = 1;
        while (sum < n) {
            sum += i;
            if (sum == n) return i;
            else if (sum > n) return i - 1;
            i++;
        }
        return i - 1;
    }
}