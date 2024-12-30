class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        

        def  dfs(pattern_idx, s_idx, to_mappings, from_mappings):
            if pattern_idx == len(pattern) and s_idx == len(s):
                return True
            
            if pattern_idx >= len(pattern) or s_idx >= len(s):
                return False
            
            p_char = pattern[pattern_idx]
            
            if p_char in to_mappings:
                word = to_mappings[p_char]
                word_len = len(word)
                if s_idx + word_len > len(s) or s[s_idx: s_idx + word_len] != word:
                    return False
                return dfs(pattern_idx + 1, s_idx + word_len, to_mappings, from_mappings)
            
            for i in range(s_idx, len(s)):
                c_word = s[s_idx: i + 1]
                if c_word in from_mappings:
                    continue
                to_mappings[p_char] = c_word
                from_mappings[c_word] = p_char
                if dfs(pattern_idx + 1, i + 1, to_mappings, from_mappings):
                    return True
                del to_mappings[p_char]
                del from_mappings[c_word]
            
            return False
        return dfs(0,0,{},{})



                
