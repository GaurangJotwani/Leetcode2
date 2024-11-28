class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, sm, curr):

            if sm == target:
                tmp = [x for x in curr]
                res.append(tmp)
                return
            if sm > target:
                return
            
            if i == len(candidates):
                return
            
            #skip
            dfs(i + 1, sm, curr)

            #add
            curr.append(candidates[i])
            dfs(i, sm + candidates[i], curr)
            curr.pop()
        
        dfs(0,0,[])
        return res
            