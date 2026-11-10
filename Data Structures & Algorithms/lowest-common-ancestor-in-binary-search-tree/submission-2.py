# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.recursiveLowestCommonAncestor(root, p, q)
    
    def recursiveLowestCommonAncestor(self, top, p, q):
        if p.val < top.val and q.val < top.val:
            return self.recursiveLowestCommonAncestor(top.left, p, q)
        elif p.val > top.val and q.val > top.val:
            return self.recursiveLowestCommonAncestor(top.right, p, q)
        else:
            return top
        