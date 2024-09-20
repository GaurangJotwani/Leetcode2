class Solution:
    def maxLength(self, arr: List[str]) -> int:

        new_arr = []
        for word in arr:
            s = set()
            canAdd = True
            for c in word:
                if c in s:
                    canAdd = False
                    break
                s.add(c)
            if canAdd:
                new_arr.append(word)
        
        arr = new_arr

        res = [0]
        def helper(i, curr):
            if i == len(arr):
                tmp = "".join(curr)
                res[0] = max(res[0], len(tmp))
                return
            
            helper(i + 1, curr)

            canAdd = True
            s = set("".join(curr))
            for c in arr[i]:
                if c in s:
                    canAdd = False
                    break
            
            if canAdd:
                curr.append(arr[i])
                helper(i + 1, curr)
                curr.pop()
        
        helper(0, [])
        return res[0]

        








