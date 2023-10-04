public class Solution {
    public IList<IList<int>> Subsets(int[] nums) {
        IList<IList<int>> res = new List<IList<int>>();
        List<int> curr = new List<int>();
        Helper(curr, nums, 0, ref res);
        return res;
    }
    
    public void Helper(List<int> curr, int[] nums, int idx, ref IList<IList<int>> res) {
        if (idx == nums.Length) {
            IList<int> copy = new List<int>();
            foreach (int num in curr) {
                copy.Add(num);
            }
            res.Add(copy);
            return;
        }
        
        curr.Add(nums[idx]);
        Helper(curr, nums, idx + 1, ref res);
        curr.RemoveAt(curr.Count() - 1);
        Helper(curr, nums, idx + 1, ref res);
        
    }
}