public class Solution {
    public bool ValidateStackSequences(int[] pushed, int[] popped) {
        int j = 0;
        var stk = new Stack<int>();

        for (int i = 0; i < pushed.Length; i++) {
            while (stk.Count > 0 && stk.Peek() == popped[j]) {
                stk.Pop(); j++;
            }
            stk.Push(pushed[i]);
        }
        while (stk.Count > 0 && stk.Peek() == popped[j]) {
                stk.Pop(); j++;
        }
        return stk.Count == 0;
    }
}