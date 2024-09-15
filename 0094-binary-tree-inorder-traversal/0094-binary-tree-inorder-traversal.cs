/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    List<int> res;
    public IList<int> InorderTraversal(TreeNode root) {
        res = new List<int>();
        helper(root);
        return res;
    }
    private void helper(TreeNode root) {
        if (root == null) return;
        helper(root.left);
        res.Add(root.val);
        helper(root.right);
    }
}