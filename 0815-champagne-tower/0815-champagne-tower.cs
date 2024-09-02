public class Solution {
    public double ChampagneTower(int poured, int query_row, int query_glass) {
        var prev_row = new double[1];
        prev_row[0] = (double) poured;

        for (int row = 1; row <= query_row; row++) {
            var cur_row = new double[row + 1];
            for (int i = 0; i < prev_row.Length; i++) {
                double extra = prev_row[i] - 1; 
                if (extra > 0) {
                    cur_row[i] += 0.5 * extra;
                    cur_row[i + 1] += 0.5 * extra;
                }
            }
            prev_row = cur_row;
        }

        return Math.Min(1, prev_row[query_glass]);

    }
}