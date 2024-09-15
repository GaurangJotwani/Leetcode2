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
    public IList<int> PreorderTraversal(TreeNode root) {
        res = new List<int>();
        PreOrder(root);
        return res;
    }

    private void PreOrder(TreeNode root) {
        if (root == null) return;
        res.Add(root.val);
        PreOrder(root.left);
        PreOrder(root.right);
    }
}