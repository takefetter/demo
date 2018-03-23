# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        bhead = ListNode(pHead.val - 1)
        bhead.next = pHead
        first_node = bhead
        second_node = pHead
        while second_node and second_node.next:
            if second_node.val == second_node.next.val:
                del_val = second_node.val
                while second_node and (second_node.val == del_val):
                    second_node = second_node.next
                first_node.next = second_node
            else:
                first_node = first_node.next
                second_node = second_node.next
        return bhead.next
