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
    int res;
    void countGoodNodes(TreeNode* root, int minVal) {
        if (root == NULL) return;
        if (root->val >= minVal) res++;
        countGoodNodes(root -> left, max(root->val, minVal));
        countGoodNodes(root -> right, max(root->val, minVal));
    }

    int goodNodes(TreeNode* root) {
        res = 0;
        countGoodNodes(root, INT_MIN);
        return res;
    }
};