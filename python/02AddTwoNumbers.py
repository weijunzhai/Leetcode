# Definition for singly-linked list.

import random


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        carry = 0
        while (l1 is not None) or (l2 is not None) or (not carry == 0):
            a1 = 0 if l1 is None else l1.val
            a2 = 0 if l2 is None else l2.val
            carry, a = divmod((a1 + a2 + carry), 10)
            node.next = ListNode(a)
            node = node.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        return head.next
          
    def generateNodeList(self, a):
        root = ListNode(0)
        head = root
        for i in range(a):
            head.next = ListNode(random.randint(0, 9))
            head = head.next
        return root.next

    def printListNode(self, l1):
        list = []
        while not l1 is None:
            list.append(l1.val)
            l1 = l1.next
        print list


if __name__ == '__main__':
    obj = Solution()
    l1 = obj.generateNodeList(3)
    l2 = obj.generateNodeList(4)
    obj.printListNode(l1)
    obj.printListNode(l2)
    l3 = obj.addTwoNumbers(l1, l2)
    obj.printListNode(l3)
    # print l1