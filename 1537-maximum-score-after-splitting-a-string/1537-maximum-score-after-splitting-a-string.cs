public class Solution {
    public int MaxScore(string s) {
        
        int sum = 0;
        foreach(var c in s) sum += int.Parse(c.ToString());

        int cSum = 0, res = 0;
        for (int i = 0; i < s.Length - 1; i++) {
            cSum += int.Parse(s[i].ToString());
            int numZeroes = i - cSum + 1;
            int numOnes = sum - cSum;
            res = Math.Max(res, numOnes + numZeroes);
        }

        return res;
    }
}