#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val  = x
        self.next = None

    def print(self):
        cur = self
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()


class Solution:
    @staticmethod
    def list_to_num2(listnode):
        summation  = 0
        radix      = 1
        summation += listnode.val * radix
        radix     *= 10
        while listnode.next is not None:
            listnode   = listnode.next
            summation += listnode.val * radix
            radix     *= 10
        return summation

    @staticmethod
    def list_to_num(listnode):
        string = ''
        while listnode is not None:
            string += str(listnode.val)
            listnode = listnode.next
        return int(string[::-1])

    @staticmethod
    def num_to_list2(num):
        digit = num%10
        pre_listnode = ListNode(digit)
        head = pre_listnode
        num = num//10
        while num != 0:
            digit = num%10
            cur_listnode      = ListNode(digit)
            pre_listnode.next = cur_listnode
            pre_listnode      = cur_listnode
            num = num//10
        return head

    @staticmethod
    def num_to_list(num):
        string = str(num)[::-1]
        head = prev = None
        for ch in string:
            cur = ListNode(int(ch))
            if prev is not None:
                prev.next = cur
            prev = cur
            if head is None:
                head = cur
        return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = Solution.list_to_num(l1)
        num2 = Solution.list_to_num(l2)
        summation = num1 + num2
        return Solution.num_to_list(summation)


def test():
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l1.print()

    l4 = ListNode(5)
    l5 = ListNode(6)
    l6 = ListNode(4)
    l4.next = l5
    l5.next = l6
    l4.print()

    # print(Solution.list_to_num(l1))
    # Solution.num_to_list(807).print()

    s = Solution()
    s.addTwoNumbers(l1, l4).print()


if __name__ == '__main__':
    # test()
    pass


