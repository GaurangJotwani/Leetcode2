public class Solution {
    public bool MakeEqual(string[] words) {
        int n = words.Length;
        var counts = new Dictionary<char, int>();

        foreach (var word in words) {
            foreach (var c in word) {
                if (!counts.ContainsKey(c)) counts[c] = 1;
                else counts[c]++;
            }
        }

        foreach(var kvp in counts) {
            if (kvp.Value % n != 0) return false;
        }

        return true;
    }
}