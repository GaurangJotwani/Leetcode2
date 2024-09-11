public class Solution {
    public bool BackspaceCompare(string s, string t) {
        Console.WriteLine(strProcessorHelper(s) + "==" + strProcessorHelper(t));
        return strProcessorHelper(s) == strProcessorHelper(t);
    }

    private string strProcessorHelper(string s) {
        var stk = new Stack<char>();
        foreach (var c in s) {
            if (c == '#') {
                if (stk.Count > 0) stk.Pop();
            } else stk.Push(c);
        }
        var res = "";
        while (stk.Count > 0) {
            res = stk.Peek() + res;
            stk.Pop();
        }
        return res;
    }
}