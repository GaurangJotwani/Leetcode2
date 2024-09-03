public class Solution {
    public int BagOfTokensScore(int[] tokens, int power) {
        Array.Sort(tokens);
        var n = tokens.Length;
        var res = 0;
        var l = 0; 
        var r = n - 1;
        var c_score = 0;

        while (l <= r) {
            if (power >= tokens[l]) {
                // play face up
                res = Math.Max(++c_score, res);
                power -= tokens[l++];
            } else if (c_score >= 1) {
                c_score--;
                power += tokens[r--];
            } else return res;
        }
        return res;

    }
}