# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) <= 0:
            return False
        root = sequence[-1]
        length = len(sequence)
        if min(sequence) > root or max(sequence) < root:
            return True  # 二叉树只有一个子树的情况下是后序遍历

        index = 0
        for i in range(length - 1):  # 用index分割左右子树
            index = i
            if sequence[i] > root:
                break
        # 由于默认sequence[index]>root所以可以从index+1开始
        for j in range(index + 1, length - 1):
            if sequence[j] < root:
                return False

        left = True
        right = True
        if index > 0:  # 存在左子树，递归左子树
            left = self.VerifySquenceOfBST(sequence[:index])
        if index < length - 1:  # 存在右子树，递归右子树
            right = self.VerifySquenceOfBST(sequence[index:length - 1])
        return left & right  # 只有当左右子树都为后序遍历时，结果为后序遍历
