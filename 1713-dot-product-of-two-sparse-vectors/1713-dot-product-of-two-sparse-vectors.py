class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = []
        for i,num in enumerate(nums):
            if num != 0:
                self.v.append((i,num)) 

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        p1,p2 = 0,0
        total = 0
        while p1 < len(self.v) and p2 < len(vec.v):
            if self.v[p1][0] == vec.v[p2][0]:
                total += self.v[p1][1] * vec.v[p2][1]
                p1 += 1
                p2 += 1
            elif self.v[p1][0] < vec.v[p2][0]:
                p1 += 1
            else:
                p2 += 1
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)