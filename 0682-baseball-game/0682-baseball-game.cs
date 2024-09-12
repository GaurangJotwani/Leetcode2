public class Solution {
    public int CalPoints(string[] operations) {
        var stk = new Stack<int>();
        foreach (var o in operations) {
            if (o == "C") stk.Pop();
            else if (o == "D") stk.Push(stk.Peek() * 2);
            else if (o == "+") {
                int num1 = stk.Peek();
                stk.Pop();
                int num3 = stk.Peek() + num1;
                stk.Push(num1);
                stk.Push(num3);
            } else stk.Push(int.Parse(o));
        }

        int res = 0;
        while (stk.Count > 0) {
            res += stk.Peek();
            stk.Pop();
        }
        return res;
    }
}