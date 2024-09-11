public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        int n = nums.Length, l = 0;
        var hs = new HashSet<int>();


        for(int r = 0; r < n; r++) {
            if (r - l > k) hs.Remove(nums[l++]);

            if (hs.Contains(nums[r])) return true;
            hs.Add(nums[r]);
        }

        return false;

        return false;

    }
}