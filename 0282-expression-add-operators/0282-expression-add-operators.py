class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        res = []

        def dfs(cur_idx, cur_res, c_sum, prev):
            if cur_idx >= len(num):
                if c_sum == target:
                    res.append("".join(cur_res))
                return
            
            for i in range(cur_idx, len(num)):
                c_str = num[cur_idx:i + 1]
                c_num = int(c_str)
                if not cur_res:
                    dfs(i + 1, [c_str], c_num, c_num)
                else:
                    dfs(i + 1, cur_res + ["+"] + [c_str], c_sum + c_num, c_num)
                    dfs(i + 1, cur_res + ["-"] + [c_str], c_sum - c_num, -c_num)
                    dfs(i + 1, cur_res + ["*"] + [c_str], c_sum - prev + prev * c_num, c_num * prev)
                
                if num[cur_idx] == "0":
                    break
        dfs(0, [], 0, 0)
        return res