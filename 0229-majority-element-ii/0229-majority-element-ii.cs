public class Solution {
    public IList<int> MajorityElement(int[] nums) {
        var res = new List<int>();
        int elem1 = -1;
        int elem2 = -1;
        int sum1 = 0;
        int sum2 = 0;

        foreach(var num in nums) {
            if (elem1 == num) sum1++;
            else if (elem2 == num) sum2++;
            else if (sum1 == 0) {
                sum1++;
                elem1 = num;
            } else if (sum2 == 0) {
                sum2++;
                elem2 = num;
            } 
            
            else {
                sum1--;
                sum2--;
            }
        }
        int cnt1 = 0;
        int cnt2 = 0;
        foreach (var num in nums) {
            if (num == elem1) cnt1++;
            else if (num == elem2) cnt2++;
        }
        int threshHold = (nums.Length / 3) + 1;
        Console.WriteLine(elem1 + " " + elem2 + " " + threshHold);
        Console.WriteLine(cnt1 + " " + cnt2 + " " + threshHold);
        if (cnt1 >= threshHold) res.Add(elem1);
        if (cnt2 >= threshHold) res.Add(elem2);
        return res;
    }
}