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
    bool isSubHelper(TreeNode* root, TreeNode* subRoot) {
        if (subRoot == NULL and root == NULL) return true;
        if (subRoot == NULL || root == NULL) return false;
        return root->val == subRoot->val and isSubHelper(root->left, subRoot->left) and isSubHelper(root->right, subRoot->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == NULL) return false;
        // Check if current root matches subRoot
        if (isSubHelper(root, subRoot)) return true;
        // Otherwise, continue searching in the left and right subtrees
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};