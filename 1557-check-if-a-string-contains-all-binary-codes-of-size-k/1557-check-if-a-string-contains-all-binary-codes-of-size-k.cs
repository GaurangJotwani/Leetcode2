public class Solution {
    

    public bool HasAllCodes(string s, int k) {
        if (k > s.Length) return false;
        HashSet<string> binaryCodes = new HashSet<string>();

        for (int r = 0; r < s.Length - k + 1; r++) {
            string key = s.Substring(r, k);
            binaryCodes.Add(key);
        }
        return binaryCodes.Count == (1 << k);
    }
}