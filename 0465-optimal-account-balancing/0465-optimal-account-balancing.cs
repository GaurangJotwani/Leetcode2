public class Solution {
    public int MinTransfers(int[][] transactions) {
        int[] amounts = new int[12];
        
        // Calculate the net balance of each person
        foreach (var t in transactions) {
            amounts[t[0]] -= t[2];  // Debt
            amounts[t[1]] += t[2];  // Credit
        }
        
        // Filter out non-zero balances
        List<int> balances = new List<int>();
        foreach (var amount in amounts) {
            if (amount != 0) balances.Add(amount);
        }
        
        return dfsHelper(0, balances);
    }

    private int dfsHelper(int start, List<int> balances) {
        // Skip settled balances
        while (start < balances.Count && balances[start] == 0) {
            start++;
        }
        
        if (start == balances.Count) return 0;

        int ans = int.MaxValue;
        for (int i = start + 1; i < balances.Count; i++) {
            // Only attempt to settle with opposite sign
            if (balances[i] * balances[start] < 0) {
                balances[i] += balances[start];
                ans = Math.Min(ans, 1 + dfsHelper(start + 1, balances));
                balances[i] -= balances[start];  // backtrack
            }
        }
        
        return ans;
    }
}