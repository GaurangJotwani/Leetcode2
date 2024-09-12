public class Solution {
    public string RemoveKdigits(string num, int k) {
        if (k >= num.Length) return "0";
        
        var stk = new Stack<char>();
        foreach (var c in num) {
            while (stk.Count > 0 && stk.Peek() > c && k > 0) {
                stk.Pop();
                k--;
            }
            stk.Push(c);
        }
        
        // If k is still greater than 0, remove the remaining digits from the end
        while (k > 0) {
            stk.Pop();
            k--;
        }
        
        // Construct the result string from the stack
        var res = new StringBuilder();
        while (stk.Count > 0) {
            res.Insert(0, stk.Pop());
        }
        
        // Remove leading zeros
        while (res.Length > 0 && res[0] == '0') {
            res.Remove(0, 1);
        }
        
        // If result is empty, return "0"
        return res.Length == 0 ? "0" : res.ToString();
    }
}
