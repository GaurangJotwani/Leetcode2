class Solution:

    def __init__(self, nums: List[int]):
        
        self.d = defaultdict(list)

        for i,num in enumerate(nums):
            self.d[num].append(i)

    def pick(self, target: int) -> int:
        lst = self.d[target]

        random_idx = randint(0, len(lst) - 1)
        return lst[random_idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)