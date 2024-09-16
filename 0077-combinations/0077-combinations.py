class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def helper(i, cur):
            if i == n + 1:
                if len(cur) == k:
                    copy_list = cur[:]
                    res.append(copy_list)
                return

            if len(cur) < k:
                cur.append(i)
                helper(i + 1, cur)
                cur.pop()

            helper(i + 1, cur)
        
        helper(1, [])
        return res
         