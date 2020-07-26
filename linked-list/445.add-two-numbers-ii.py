#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (53.88%)
# Likes:    1463
# Dislikes: 154
# Total Accepted:    160.9K
# Total Submissions: 295.8K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def list2num(self, listnode):
        summ = ''
        cur = listnode
        while cur:
            summ += str(cur.val)
            cur = cur.next
        return int(summ)

    def num2list(self, num):
        num = str(num)
        dummy = ListNode()
        cur = dummy
        for n in num:
            tmp = ListNode(n)
            cur.next = tmp
            cur = cur.next
        return dummy.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.list2num(l1)
        num2 = self.list2num(l2)
        summ = num1 + num2
        return self.num2list(summ)

# @lc code=end

