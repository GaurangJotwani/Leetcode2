class Solution:
    def maximumSwap(self, num: int) -> int:
        
        

        num_str = list(str(num))

        max_right = [-1] * len(num_str)
        cur_max = float("-inf")
        c_idx = -1

        for i in range(len(num_str) - 1, -1, -1):
            cNum = int(num_str[i])
            if cNum > cur_max:
                cur_max = cNum
                c_idx = i
            max_right[i] = (cur_max, c_idx)
        
        for i,num in enumerate(num_str):
            num = int(num)
            if max_right[i][0] > num:
                num_str[i] = str(max_right[i][0])
                num_str[max_right[i][1]] = str(num)
                break
        
        return int("".join(num_str))


