public class Solution {
    public IList<string> FindRepeatedDnaSequences(string s) {
        var res = new List<string>();
        if (s.Length < 10) return res;
        var counts = new Dictionary<string, int>();
        
        for (int i = 0; i <= s.Length - 10; i++) {
            var sequence = s.Substring(i, 10);
            if (counts.ContainsKey(sequence)) {
                counts[sequence]++;
                if (counts[sequence] == 2) res.Add(sequence);
            } else {
                counts[sequence] = 1;
            }
        }
        return res;
    }
}
