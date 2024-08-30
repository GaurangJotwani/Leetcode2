public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        var res = new List<IList<int>>();
        for (int i = 1; i <= numRows; i++) {
            var temp = new List<int>();
            for (int j = 1; j <= i; j++) {
                
                if (j == 1 || j == i) temp.Add(1);
                else {
                    temp.Add(res[i - 2][j - 2] + res[i - 2][j-1]);
                } 
                
            }
            res.Add(temp);
        }
        return res;
    }
}