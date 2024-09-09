public class Solution {
    public string DecodeString(string s) {
        var stk = new Stack<string>();

        foreach (var c in s) {
            if (c != ']') {
                stk.Push(c.ToString());
                continue;
            }
            var sb = "";
            while (stk.Peek() != "[") {
                sb = stk.Peek() + sb;
                stk.Pop();
            }

            stk.Pop();
            var digit_string = "";
            while (stk.Count > 0 && char.IsDigit(stk.Peek()[0])) {
                digit_string = stk.Peek() + digit_string;
                stk.Pop();
            }

            var dig = int.Parse(digit_string);
            var cur = sb.ToString();
            for (int i = 0; i < dig - 1; i++) sb += (cur);
            stk.Push(sb.ToString());
        }

        var charArr = stk.ToArray();
        Array.Reverse(charArr);
        return string.Join("", charArr);
    }
}