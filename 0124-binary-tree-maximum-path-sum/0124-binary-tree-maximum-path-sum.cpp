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
    int res = INT_MIN;
    int maxPathSum(TreeNode* root) {
        
        dfs(root);
        return res;
    }
private: 
    int dfs(TreeNode* root) {
        if (root == NULL) return 0;
        
        int left = dfs(root -> left);
        int right = dfs(root -> right);
        
        int inLine = max(root-> val, max(left, right) + root -> val);
        int inRoot = max(inLine, root -> val + left + right);
        res = max(res, inRoot);
        
        return inLine;
    }
};