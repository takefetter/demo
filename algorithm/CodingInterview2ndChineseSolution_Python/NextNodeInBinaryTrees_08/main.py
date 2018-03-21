from algorithm.CodingInterview2ndChineseSolution_Python.ConstructBinaryTree_07.main import Solution as BTree
##无法运行,

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return
        if pNode.right:
            temp = pNode.right
            while temp.left:
                temp = temp.left
            return temp
        else:
            if pNode.next is None:
                return
            elif pNode.next.left == pNode:
                return pNode.next
            else:
                if pNode.next.next.left == pNode.next:
                    return pNode.next.next
                else:
                    return


def main():
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    a = BTree().reConstructBinaryTree(pre=pre, tin=tin)
    b = Solution().GetNext(a)
    print(b)


if __name__ == '__main__':
    main()
