public class Solution {
    public string MakeGood(string s) {
        var stk = new Stack<char>();
        foreach (var c in s) {
            if (stk.Count > 0 && char.ToLower(c) == char.ToLower(stk.Peek())) {
                if (char.IsLower(c) && char.IsUpper(stk.Peek()) || char.IsUpper(c) && char.IsLower(stk.Peek())) {
                    stk.Pop();
                    continue;
                }
            }
            stk.Push(c);
        }
        var res = "";
        while (stk.Count > 0) {
            var c = stk.Peek();
            stk.Pop();
            res = c + res;
        }
        return res;
    }
}