# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        curr = []
        def dfs(node):
            if not node:
                curr.append("N")
                return
            curr.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(curr)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        idx = [0]
        def dfs():
            if data[idx[0]] == "N":
                idx[0] += 1
                return None
            new_node = TreeNode(int(data[idx[0]]))
            idx[0] += 1
            new_node.left = dfs()
            new_node.right = dfs()
            return new_node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))