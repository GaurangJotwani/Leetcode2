public class Solution {
    public int MaxLengthBetweenEqualCharacters(string s) {

        var firstSeen = new int[26];
        for (var i = 0; i < 26; i++) firstSeen[i] = -1;
        int res = -1, n = s.Length;

        for (var i = 0; i < n; i++) {
            if(firstSeen[s[i] - 'a'] != -1) res = Math.Max(i - firstSeen[s[i] - 'a'] - 1, res);
            else firstSeen[s[i] - 'a'] = i;
        }

        return res;

    }
}