class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0] * len(w)
        sm = 0
        for i,num in enumerate(w):
            sm += num
            self.prefix_sum[i] = sm
        self.total = self.prefix_sum[-1]
        

    def pickIndex(self) -> int:

        random_num = random.randint(1, self.total)
        return self.binary_search(random_num)
    
    def binary_search(self, random_num):
        l = 0
        r = len(self.prefix_sum) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if self.prefix_sum[mid] == random_num:
                return mid
            if random_num < self.prefix_sum[mid]:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()