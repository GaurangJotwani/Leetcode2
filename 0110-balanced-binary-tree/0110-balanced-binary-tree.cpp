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
    bool res;
    int dfs(TreeNode* root) {
        if (root == NULL) return 0;
        int l = dfs(root->left);
        int r = dfs(root->right);
        cout << l <<" " << r << endl;
        if (abs(r - l) > 1) {
            res = false;
        }
        return 1 + max(l, r);
    }
    bool isBalanced(TreeNode* root) {
        if (root == NULL) return true;
        res = true;
        dfs(root);
        return res;
    }
};