class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        dp = [(1, 1)] * len(nums)
        longest = 1
        res = 1

        for i in range(1, len(nums)):
            num = nums[i]
            tmp = 1
            freq = 1
            for j in range(i - 1, -1, -1):
                if nums[j] < num:
                    curr = 1 + dp[j][0]
                    if curr > tmp:
                        tmp = curr
                        freq = dp[j][1]
                    elif curr == tmp:
                        freq += dp[j][1]
                
            dp[i] = (tmp, freq)
            if tmp > longest:
                longest = tmp
                res = freq
            elif tmp == longest:
                res += freq
        
        return res

                




        