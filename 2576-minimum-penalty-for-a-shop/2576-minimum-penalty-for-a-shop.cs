public class Solution {
    public int BestClosingTime(string customers) {
        
        int total = 0; 
        foreach(var c in customers) {
            if (c == 'Y') total++;
        }
        int ans = 0, minPenalty = total;
        for (int i = 0; i < customers.Length; i++) {
            char c = customers[i];
            if (c == 'Y') {
                total--;
                if (total < minPenalty) {
                    ans = i + 1;
                    minPenalty = total; 
                }
            } else total++;
        }

        return ans;
    }
}