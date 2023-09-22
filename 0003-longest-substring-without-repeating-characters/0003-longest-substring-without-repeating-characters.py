class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            c_char = s[right]
            while c_char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(c_char)
            longest = max(longest, len(seen))
        

        return longest



        