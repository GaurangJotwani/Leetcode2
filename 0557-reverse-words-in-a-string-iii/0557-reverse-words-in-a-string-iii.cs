public class Solution {
    public string ReverseWords(string s) {
        string[] words = s.Split(" ");
        for (int i = 0; i < words.Length; i++) {
            var word = words[i].ToCharArray();
            Array.Reverse(word);
            var rev = new string(word);
            words[i] = rev;
        }

        return string.Join(" ", words);
    }
}