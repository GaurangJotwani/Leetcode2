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
    bool isBalanced(TreeNode* root) {
        bool res = true;
        helper(root, res);
        return res;
    }
    
    int helper(TreeNode* root, bool& res) {
        if (root == NULL) return 0;
        
        int left = helper(root->left, res);
        int right = helper(root-> right, res);
        if (abs(right - left) > 1) {
            res = false;
        }
        return 1 + max(left, right);
    }
};