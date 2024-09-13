public class Solution {
    public string RemoveDuplicates(string s, int k) {
        var letters = new Stack<(char c, int freq)>();
        foreach (char c in s) {
            if (letters.Count > 0 && letters.Peek().c == c) {
                var pair = letters.Peek();
                letters.Pop();
                if (pair.freq + 1 == k) continue;
                else letters.Push((c, pair.freq + 1));
            } else letters.Push((c, 1));
        }
        var res = new List<char>();
        while (letters.Count > 0) {
            var pair = letters.Peek();
            letters.Pop();
            for (int i = 0; i < pair.freq; i++) res.Add(pair.c);
        }
        res.Reverse();
        return new string(res.ToArray());
    }
}