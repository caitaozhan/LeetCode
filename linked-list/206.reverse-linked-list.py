#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (58.16%)
# Likes:    3191
# Dislikes: 77
# Total Accepted:    763K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution4:
    '''using a stack'''
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        dummy = ListNode(0)
        cur = dummy
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return dummy.next
    

class Solution3:
    '''using divide and conquer'''

    def reserve_helper(self, head):
        '''given a head of a list, reverse it and return the reversed list's head and tail
        '''
        if head is None:
            return None, None

        rest = head.next
        rest_rev_head, rest_rev_tail = self.reserve_helper(rest)
        if rest_rev_head is None:
            return head, head
        rest_rev_tail.next = head
        head.next = None
        return rest_rev_head, head

    def reverseList(self, head: ListNode) -> ListNode:
        head, _ = self.reserve_helper(head)
        return head


class Solution2:
    '''iteratively without a stack'''
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre
         

class Solution:
    '''Recursive, but not divide and conquer'''
    def reverseList(self, head: ListNode) -> ListNode:
        '''given a head, reverse the current head's left side and right side, 
           return the final revsered linked list's head
        '''
        if head is None or head.next is None:
            return head
        final_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return final_head

# @lc code=end

