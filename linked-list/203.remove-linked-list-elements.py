#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (37.57%)
# Likes:    1559
# Dislikes: 88
# Total Accepted:    323.8K
# Total Submissions: 861K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = None
        cur = head
        while cur is not None:
            if cur.val == val:
                cur = cur.next
                if pre is None:
                    head = head.next  # one wrong submission here
                else:
                    pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return head


# @lc code=end

