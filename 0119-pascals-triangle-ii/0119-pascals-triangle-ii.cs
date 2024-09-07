public class Solution {
    public IList<int> GetRow(int rowIndex) {
        var prev = new int[1];
        prev[0] = 1;
        if (rowIndex == 0) return prev;

        for (int row = 1; row <= rowIndex; row++) {
            var nxt = new int[row + 1];
            for (int i = 0; i < row + 1; i++) {
                if (i == 0) nxt[i] = 1;
                else if (i == row) nxt[i] = 1;
                else nxt[i] = prev[i - 1] + prev[i];
            }
            prev = nxt;
        }

        return prev;


    }
}