class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        curr_len = 1
        res = ""
        while True:
            if curr_len > len(strs[0]):
                return res
            c_prefix = strs[0][:curr_len]
            for s in strs:
                if len(c_prefix) > len(s) or not s.startswith(c_prefix):
                    return res
            curr_len += 1
            res = c_prefix
        

                
        