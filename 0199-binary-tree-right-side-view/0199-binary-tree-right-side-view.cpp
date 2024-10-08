/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (root == NULL) return {};
        queue<TreeNode*> q;
        q.push(root);
        vector<int> res;
        while (!q.empty()) {
            int l = q.size();
            res.push_back(q.front()->val);
            for (int i = 0; i < l; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node->right != NULL) {
                    q.push(node->right);
                }
                if (node->left != NULL) {
                    q.push(node->left);
                }
            }
        }
        return res;
    }
};