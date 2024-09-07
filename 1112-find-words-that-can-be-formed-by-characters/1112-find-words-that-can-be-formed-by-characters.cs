public class Solution {
    public int CountCharacters(string[] words, string chars) {
        var seen = new Dictionary<char, int>(); 
        foreach(var c in chars) {
            if (seen.ContainsKey(c)) seen[c]++;
            else seen[c] = 1;
        }

        int res = 0;

        foreach (var word in words) {
            bool isGood = true;
            var freq = new Dictionary<char, int>();
            foreach (var c in word) {
                if (!seen.ContainsKey(c)) {
                    isGood = false;
                    break;
                }
                if (freq.ContainsKey(c)) freq[c]++;
                else freq[c] = 1;
                if (freq[c] > seen[c]) {
                    isGood = false;
                    break;
                }

            }
            if (isGood) res += word.Length;
        }
        return res;
    }
}