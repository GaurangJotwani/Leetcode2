class Solution:
    def maximumLength(self, s: str) -> int:

        res = -1
        counter = defaultdict(int)


        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j + 1]
                if len(set(substr)) == 1:
                    counter[substr] += 1
                    if counter[substr] >= 3:
                        res = max(res, len(substr))
        

        return res

                
        