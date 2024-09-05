public class Solution {
    public string RemoveStars(string s) {
        var stk = new Stack<char>();

        foreach (var c in s) {
            if (c == '*') {
                if (stk.Count != 0) stk.Pop();
            } else {
                stk.Push(c);
            }
        }
        var sb = new StringBuilder();
        while (stk.Count != 0) {
            var c = stk.Peek();
            stk.Pop();
            sb.Append(c);
        }
        var a = new string(sb.ToString().Reverse().ToArray());
        return a;
    }
}