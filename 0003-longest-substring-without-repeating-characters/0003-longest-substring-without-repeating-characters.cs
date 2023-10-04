public class Solution {
    public int LengthOfLongestSubstring(string s) {
        
        HashSet<char> seen = new HashSet<char>();
        int longest = 0;
        int left = 0;
        
        for (int right = 0; right < s.Length; right++) {
            if (!seen.Contains(s[right])) {
                seen.Add(s[right]);
                longest = Math.Max(longest, right - left + 1);
                continue;
            }
            seen.Remove(s[left]);
            right -= 1;
            left += 1;
        }
        
        
        
        
        
        
        return longest;
        
        
    }
}