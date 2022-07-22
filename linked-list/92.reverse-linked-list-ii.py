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



class Solution:
    '''doing again on 7/21/2022
       partition the list into left, middle, right
    '''
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        # step 1: segment the list
        node_before_left = None
        node_after_right = None
        node_right = None
        node_left = None
        dummy = ListNode(0, head)
        cur = dummy
        counter = 0
        while cur:
            if counter == left - 1:
                node_before_left = cur
                node_left = cur.next
            if counter == right:
                node_right = cur
                node_after_right = cur.next
                break
            cur = cur.next
            counter += 1
        # step 2: reverse the middle segment
        prev = node_left
        cur = prev.next
        while cur != node_after_right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # step 3: concatinate the middle segment with left and right
        node_before_left.next = node_right
        node_left.next = node_after_right
        
        return dummy.next

# @lc code=end

