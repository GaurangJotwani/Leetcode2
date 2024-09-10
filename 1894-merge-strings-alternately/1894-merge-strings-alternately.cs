public class Solution {
    public string MergeAlternately(string word1, string word2) {
        var sb = new StringBuilder();
        int p1 = 0, p2 = 0;
        while (p1 < word1.Length && p2 < word2.Length) {
            Console.WriteLine($"{p1} - {p2}");
            sb.Append(word1[p1++]);
            sb.Append(word2[p2++]);
            
        }

        while (p1 < word1.Length) sb.Append(word1[p1++]);
        while (p2 < word2.Length) sb.Append(word2[p2++]);

        return sb.ToString();
    }
}