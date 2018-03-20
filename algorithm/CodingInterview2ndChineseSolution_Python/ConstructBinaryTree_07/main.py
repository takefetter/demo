# -*- coding:utf-8 -*-
'''''
重建二叉树
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            res = TreeNode(pre[0])
            res.left = self.reConstructBinaryTree(pre[1: tin.index(pre[0]) + 1], tin[: tin.index(pre[0])])
            res.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])
        return res

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print(root.val)
        self.front_digui(root.left)
        self.front_digui(root.right)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.left)
        print(root.val)
        self.middle_digui(root.right)

    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.left)
        self.later_digui(root.right)
        print(root.val)

    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                print(node.val)
                myStack.append(node)
                node = node.left
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right  # 开始查看它的右子树

    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.left
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.val)
            node = node.right  # 开始查看它的右子树

    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:  # 将myStack2中的元素出栈，即为后序遍历次序
            print(myStack2.pop().val)

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val)
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)


def main():
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    a = Solution().reConstructBinaryTree(pre=pre, tin=tin)

    # Solution.front_digui(self=Solution(), root=a)
    # Solution.middle_digui(self=Solution(), root=a)
    Solution.later_digui(self=Solution(), root=a)
    print('\n')
    # Solution.front_stack(self=Solution(), root=a)
    # Solution.middle_stack(self=Solution(), root=a)
    Solution.later_stack(self=Solution(), root=a)


if __name__ == '__main__':
    main()
