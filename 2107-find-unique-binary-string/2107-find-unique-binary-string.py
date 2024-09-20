class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        seen = set(nums)
        n = len(nums)
        ans = [""]

        def dfs(curr):
            if len(curr) == n:
                res = "".join(curr)
                if res not in seen:
                    ans[0] = res
                    return True
                return False
            
            curr.append("0")
            if dfs(curr):
                return True
            curr.pop()

            curr.append("1")
            if dfs(curr):
                return True
            curr.pop()

            return False
        
        dfs([])
        return ans[0]
            
            


        