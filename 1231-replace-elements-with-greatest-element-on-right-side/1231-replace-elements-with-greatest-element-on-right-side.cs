public class Solution {
    public int[] ReplaceElements(int[] arr) {
        
        int n = arr.Length;
        int c_max = arr[n - 1];
        arr[n - 1] = -1;
        for (int i = n - 2; i >= 0; i--) {
            int tmp = arr[i];
            arr[i] = c_max;
            c_max = Math.Max(tmp, arr[i]);
        }
        return arr;

    }
}