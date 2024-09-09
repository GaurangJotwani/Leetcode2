public class Solution {
    public int[] AsteroidCollision(int[] asteroids) {
        var stk = new Stack<int>();

        foreach (int num in asteroids) {
            if (stk.Count == 0 || num > 0) {
                stk.Push(num);
                continue;
            }
            
            if (stk.Peek() < 0) {
                stk.Push(num);
                continue;
            }

            while (stk.Count != 0 && stk.Peek() > 0 && Math.Abs(num) > stk.Peek()) stk.Pop();
            if (stk.Count == 0 || stk.Peek() < 0) stk.Push(num);
            else if (stk.Peek() == Math.Abs(num)) stk.Pop();

            
        }

        var arr = stk.ToArray();
        Array.Reverse(arr);
        return arr;
    }
}