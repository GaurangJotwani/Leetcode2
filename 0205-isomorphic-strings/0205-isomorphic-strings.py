class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_p, t_p = 0, 0
        charMapStT = {}
        charMapT2S = {}

        while s_p < len(s):
            char_s, char_t = s[s_p], t[t_p]
            if char_s not in charMapStT and char_t not in charMapT2S:
                charMapStT[char_s] = char_t
                charMapT2S[char_t] = char_s
                s_p += 1
                t_p += 1
                continue
            if char_s not in charMapStT or char_t not in charMapT2S:
                return False
            if charMapStT[char_s] == char_t and charMapT2S[char_t] == char_s:
                s_p += 1
                t_p += 1
                continue
            return False
        
        return True

        