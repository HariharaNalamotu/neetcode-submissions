# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = {}
        self.recursiveAdd(root, 0)
        result = [0] * len(self.levels.keys())
        for i in self.levels.keys():
            result[i] = self.levels[i]
        return result

    def recursiveAdd(self, node, depth):
        if node is None:
            return
        if depth in self.levels.keys():
            self.levels[depth].append(node.val)
        else:
            self.levels[depth] = [node.val]

        if node.left:
            self.recursiveAdd(node.left, depth + 1)

        if node.right:
            self.recursiveAdd(node.right, depth + 1)
