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
    unordered_map<int, Node*> clones;
    Node* cloneGraph(Node* node) {
        return clone_helper(node);
    }
private:
    Node* clone_helper(Node* node) {
        if (!node)
            return nullptr;
        
        if (clones.find(node->val) != clones.end()) {
            return clones[node->val];
        }
        
        Node* clone = new Node(node->val);
        clones[node->val] = clone;
        
        for (auto nei: node->neighbors) {
            clone->neighbors.push_back(clone_helper(nei));
        }
        
        return clone;
    }
};