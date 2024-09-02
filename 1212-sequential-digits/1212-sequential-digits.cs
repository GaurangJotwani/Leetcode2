public class Solution {
    List<int> res = new List<int>();

    private void digitHelper(int low, int high, int cNum) {
        if (cNum > high) return;
        if (cNum >= low && cNum <= high) res.Add(cNum);
        int lastDig = cNum % 10;
        if (lastDig == 9) return;
        lastDig++;
        digitHelper(low, high, (cNum * 10) + lastDig);
    }

    public IList<int> SequentialDigits(int low, int high) {
        for (int i = 1; i <= 8; i++) {
            digitHelper(low, high, i);
        }
        res.Sort();
        return res;
    }
}