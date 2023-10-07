public class Solution {
    public int ArraySign(int[] nums) {
        
        int prod = 1;
        int[] freq = new int[1];
        freq[0] = 0;
        
        foreach (int num in nums) {
            if (num == 0) {
                return 0;
            } else if (num < 0) {
                freq[0] += 1;
            }
        }
                
        if (freq[0] % 2 == 0) {
            return 1;
        } else {
            return -1;
        }
        
    }
}