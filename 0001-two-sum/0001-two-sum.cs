public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        Dictionary<int, int> diff = new Dictionary<int, int>();
        
        for (int i = 0; i < nums.Count(); i++) {
            int num = nums[i];
            int difference = target - num;
            if (diff.ContainsKey(difference)) {
                int[] res = new int[2];
                res[0] = diff[difference];
                res[1] = i;
                return res;
            }
            
            diff[num] = i;
        }
        
        return null;
        
        
        
        
        
    }
}