# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum1(root)
        return self.tilt

    def sum1(self, root1):
        if root1 == None:
            return 0
        left = self.sum1(root1.left)
        right = self.sum1(root1.right)
        self.tilt += abs(left - right)
        return left + right + root1.val
