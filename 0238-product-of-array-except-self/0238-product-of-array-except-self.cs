public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        
        List<int> left_products = new List<int>();
        
        int prod = 1;
        
        foreach(int num in nums) {
            left_products.Add(prod);
            prod = num * prod;
        }
        
        int[] right_prods = new int[nums.Length];
        
        prod = 1;
        
        for(int i = nums.Length - 1; i >= 0; i--) {
            right_prods[i] = prod;
            prod = nums[i] * prod;
        }
        
        int[] res = new int[nums.Length];
        
        for(int i = 0; i < nums.Length; i++) {
            res[i] = left_products[i] * right_prods[i];
        }
        
        return res;
        
    }
}