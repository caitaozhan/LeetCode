#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (48.34%)
# Likes:    2845
# Dislikes: 413
# Total Accepted:    732.4K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#



# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        last = head
        cur1 = l1
        cur2 = l2
        while cur1 or cur2:
            if cur1 is None:
                last.next = ListNode(cur2.val)
                last = last.next
                cur2 = cur2.next
            elif cur2 is None:
                last.next = ListNode(cur1.val)
                last = last.next
                cur1 = cur1.next
            else:
                if cur1.val < cur2.val:
                    last.next = ListNode(cur1.val)
                    last = last.next
                    cur1 = cur1.next
                else:
                    last.next = ListNode(cur2.val)
                    last = last.next
                    cur2 = cur2.next
        return head.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = last = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                last.next = l1
                l1 = l1.next
            else:
                last.next = l2
                l2 = l2.next
            last = last.next
        last.next = l1 or l2
        return head.next
        
# @lc code=end

