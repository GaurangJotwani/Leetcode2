class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        width = 0
        cur_line = []
        res = []
        i = 0

        while i < len(words):
            c_word = words[i]

            if len(c_word) + width <= maxWidth:
                cur_line.append(c_word)
                width += len(c_word) + 1
                i += 1
            else:
                spaces = maxWidth - width + len(cur_line)
                added = 0
                j = 0
                while spaces > added:
                    if j >= len(cur_line) - 1:
                        j = 0
                    cur_line[j] += " "
                    added += 1
                    j += 1
                
                width = 0
                res.append("".join(cur_line))
                cur_line = []
            
        # print(res)
        # print(cur_line, width)
        
        for i in range(len(cur_line) - 1):
            cur_line[i] += " "
            

        spaces = maxWidth - width + 1
        cur_line[-1] += " " * spaces

        res.append("".join(cur_line))

        return res
        





