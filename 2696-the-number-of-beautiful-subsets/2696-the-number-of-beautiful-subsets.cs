public class Solution {
    
    public int BeautifulSubsets(int[] nums, int k) {
        var curr = new List<int>();
        return GetSubsets(0, curr, nums, k);
    }

    private int GetSubsets(int idx, List<int> curr,  int[] nums, int k) {
        if (idx == nums.Length) {
            if (curr.Count > 0) return 1;
            return 0;
        }
        int ans = 0;

        // Try putting in
        bool canAdd = true;
        int cNum = nums[idx];
        foreach (var num in curr) {
            if (Math.Abs(num - cNum) == k) {
                canAdd = false;
                break;
            }
        }
        if (canAdd) {
            curr.Add(cNum);
            ans += GetSubsets(idx + 1, curr, nums, k);
            curr.RemoveAt(curr.Count - 1);
        }

        // Dont put it
        ans += GetSubsets(idx + 1, curr, nums, k);
        
        return ans;
    }
}