public class Solution {
    public int NumRescueBoats(int[] people, int limit) {
        Array.Sort(people);
        var n = people.Length;
        var ans = 0;
        var l = 0; var r = n - 1;

        while (l <= r) {
            if (l == r) return ++ans;
            if (people[l] + people[r] <= limit) {
                l++;
            }
            ans++;
            r--;
        }
        return ans;
    }
}