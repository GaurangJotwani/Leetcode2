# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        d = defaultdict(list)
        lowest = float("inf")
        highest = float("-inf")

        q = deque()
        q.append((root, 0))

        while q:
            node, num = q.popleft()
            lowest = min(lowest, num)
            highest = max(highest, num)
            d[num].append(node.val)
            if node.left:
                q.append((node.left, num -1))
            if node.right:
                q.append((node.right, num + 1))
        

        res = []
        for i in range(lowest, highest + 1):
            res.append(d[i])

        return res
        