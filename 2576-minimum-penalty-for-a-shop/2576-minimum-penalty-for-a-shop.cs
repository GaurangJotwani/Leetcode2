public class Solution {
    public int BestClosingTime(string customers) {
        int n = customers.Length;
        int sum = 0;
        for (int i = 0; i < n; i++) if (customers[i] == 'Y') sum++;
        int earliest = 0;
        int minPenalty = sum;
        int curPenalty = sum;

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