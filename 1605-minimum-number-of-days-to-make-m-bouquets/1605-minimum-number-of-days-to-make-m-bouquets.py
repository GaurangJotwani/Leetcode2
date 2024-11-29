class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if m * k > len(bloomDay):
            return -1
        l = 1
        r = max(bloomDay)
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if self.canMake(bloomDay,m,k,mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


    def canMake(self, bloomDay, m, k, days):
        i = 0
        cnt = 0
        while i < len(bloomDay) - k + 1:
            pair_found = True
            for j in range(k):
                if bloomDay[i + j] > days:
                    i = i + j + 1
                    pair_found = False
                    break
            if not pair_found:
                continue
            cnt += 1
            if cnt >= m:
                return True
            i = i + k
        return cnt >= m
        


