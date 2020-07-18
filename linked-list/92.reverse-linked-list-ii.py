#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (38.25%)
# Likes:    2359
# Dislikes: 140
# Total Accepted:    273.4K
# Total Submissions: 708K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
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

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''the list is partitioned into three segments: part1, between, part3
        '''
        dummy1 = ListNode(0, head)
        pre, cur = dummy1, head
        part1_tail, part3_head = None, None
        between1, between2 = None, None
        counter = 1

        while cur is not None:
            if counter == m:
                between1 = cur
                part1_tail = pre
            
            if m < counter <=n:
                nxt = cur.next
                cur.next = pre
                pre, cur = cur, nxt
            else:
                pre, cur = cur, cur.next
            
            if counter == n:
                part3_head = cur
                between2 = pre
            counter += 1

        part1_tail.next = between2
        between1.next = part3_head

        return dummy1.next

# @lc code=end

