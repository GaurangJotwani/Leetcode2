/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:

    Node* cloneGraph(Node* node) {
        if (node == NULL) return NULL;
        unordered_map<int, Node*> node_map;
        return dfs(node, node_map);
    }
private:
    Node* dfs(Node* node, unordered_map<int, Node*> &node_map) {
        
        if (node_map.find(node->val) != node_map.end()) return node_map[node->val];
        Node* newNode = new Node(node->val);
        node_map[node->val] = newNode;
        for (auto nei: node->neighbors) {
            newNode->neighbors.push_back(dfs(nei, node_map));
        }
        return newNode;
    }
};




















































