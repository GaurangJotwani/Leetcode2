public class Solution {
    public int FirstUniqChar(string s) {
        var d = new Dictionary<char, (int, int)>();

        for (int i = 0; i < s.Length; i++) {
            if (!d.ContainsKey(s[i])) d[s[i]] = (i, 1);
            else d[s[i]] = (d[s[i]].Item1,d[s[i]].Item2 + 1);
        }

        var lowestIdx = int.MaxValue;
        foreach (var kvp in d) {
            if (kvp.Value.Item2 == 1 && kvp.Value.Item1 < lowestIdx) lowestIdx = kvp.Value.Item1;
        }
        return lowestIdx == int.MaxValue ? -1 : lowestIdx;
    }
}