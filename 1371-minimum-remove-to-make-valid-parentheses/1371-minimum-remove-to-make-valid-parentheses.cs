public class Solution {
    public string MinRemoveToMakeValid(string s) {
        var stk = new Stack<(char, int)>();
        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            if (c == '(') stk.Push((c, i));
            else if (c == ')') {
                if (stk.Count > 0 && stk.Peek().Item1 == '(') stk.Pop();
                else stk.Push((c, i));
            }
        }
        var sb = new List<char>();
        for (int i = s.Length - 1; i >= 0; i--) {
            if (stk.Count > 0 && stk.Peek().Item2 == i) {
                stk.Pop();
                continue;
            }
            sb.Add(s[i]);
        }
        sb.Reverse();
        return new string(sb.ToArray());
    }
}