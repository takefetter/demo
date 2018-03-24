'''
题目：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，
定义其为对称的。
'''

'''
思路：二叉树镜像相同是对称的，利用递归做
34ms
6340k
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.IsSymmetrical(pRoot, pRoot)

    def IsSymmetrical(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.IsSymmetrical(pRoot1.left, pRoot2.right) and self.IsSymmetrical(pRoot1.right, pRoot2.left)
