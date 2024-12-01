"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return "N"
        curr = []
        def dfs(node):
            curr.append(str(node.val))
            curr.append(str(len(node.children)))
            for child in node.children:
                dfs(child)
        dfs(root)
        return ",".join(curr)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        data = data.split(",")
        idx = [0]
        if data[0] == "N":
            return None
        def dfs():
            new_node = Node(int(data[idx[0]]))
            idx[0] += 1
            chld_sz = int(data[idx[0]])
            idx[0] += 1
            for i in range(chld_sz):
                new_node.children.append(dfs())

            return new_node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))