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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (root == NULL) return res;
        queue<TreeNode*> q({root});
        
        while (!q.empty()) {
            int len = q.size();
            vector<int> temp;
            for (int i = 0; i< len; i++) {
                TreeNode* next = q.front();
                temp.push_back(next->val);
                if (next->left != NULL) q.push(next->left);
                if (next->right != NULL) q.push(next->right);
                q.pop();
            }
            res.push_back(temp);
        }
        
        return res;
        
    }
};