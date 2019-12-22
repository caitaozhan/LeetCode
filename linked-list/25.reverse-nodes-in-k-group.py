#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (37.41%)
# Likes:    1497
# Dislikes: 300
# Total Accepted:    217.1K
# Total Submissions: 563.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def print(self):
        print('HEAD -> ', end='')
        cur = self
        while cur is not None:
            print(cur.val, '-> ', end='')
            cur = cur.next
        print('None\n')


class Solution:
    @staticmethod
    def size(head):
        counter = 0
        cur = head
        while cur is not None:
            counter += 1
            cur = cur.next
        return counter

    @staticmethod
    def reverse_adjacent_node(node0, node1_last, node2):
        '''switch node1 and node2. node0 is a single node, node1 is a group of nodes, node2 is a single node
        '''
        node1_last.next = node2.next
        node2.next = node0.next
        node0.next = node2


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        size = Solution.size(head)
        if size == 0:
            return head
        if size < k:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        nxt = head.next
        group_size = k

        while True:
            cur_indx = 0
            while cur_indx < k - 1:
                Solution.reverse_adjacent_node(pre, cur, nxt)
                # dummy.next.print()
                nxt = cur.next
                cur_indx += 1
            group_size += k
            if group_size > size:
                break
            pre = cur
            cur = nxt
            nxt = nxt.next

        return dummy.next


def test1():
    print('--')
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l1.print()
    s = Solution()
    s.reverseKGroup(l1, 2).print()


def test2():
    print('--')
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l1.print()
    s = Solution()
    s.reverseKGroup(l1, 3).print()

def test3():
    print('--')
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l1.print()
    s = Solution()
    s.reverseKGroup(l1, 4).print()

def test4():
    print('--')
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l1.print()
    s = Solution()
    s.reverseKGroup(l1, 1).print()

def test5():
    print('--')
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    l1.print()
    s = Solution()
    s.reverseKGroup(l1, 2).print()

def test6():
    print('--')
    l1 = ListNode(1)
    l1.print()
    s = Solution()
    s.reverseKGroup(l1, 2).print()

if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

# @lc code=end

