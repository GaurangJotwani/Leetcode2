public class Solution {
    public int BestClosingTime(string customers) {
        int n = customers.Length;
        int earliest = 0;
        int minPenalty = 0;
        int curPenalty = 0;

        for (int i = 0; i < n; i++) {
            if (customers[i] == 'Y') curPenalty--;
            else curPenalty++;
            if (curPenalty < minPenalty) {
                minPenalty = curPenalty;
                earliest = i + 1;
            }
        }

        return earliest;
    }
}