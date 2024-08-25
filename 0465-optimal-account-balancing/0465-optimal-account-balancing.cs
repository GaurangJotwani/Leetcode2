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
        
        // Memoization dictionary
        Dictionary<string, int> memo = new Dictionary<string, int>();
        
        return dfsHelper(0, balances, memo);
    }

    private int dfsHelper(int start, List<int> balances, Dictionary<string, int> memo) {
        // Skip settled balances
        while (start < balances.Count && balances[start] == 0) {
            start++;
        }
        
        if (start == balances.Count) return 0;
        
        // Generate a unique key for the current state of balances and the start index
        string key = start + ":" + string.Join(",", balances);
        if (memo.ContainsKey(key)) {
            return memo[key];
        }

        int ans = int.MaxValue;
        for (int i = start + 1; i < balances.Count; i++) {
            // Only attempt to settle with opposite sign
            if (balances[i] * balances[start] < 0) {
                balances[i] += balances[start];
                ans = Math.Min(ans, 1 + dfsHelper(start + 1, balances, memo));
                balances[i] -= balances[start];  // backtrack
            }
        }

        // Store the result in the memoization dictionary
        memo[key] = ans;
        
        return ans;
    }
}