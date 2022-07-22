#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_small = ListNode()
        dummy_large = ListNode()
        cur_small = dummy_small
        cur_large = dummy_large
        cur = head
        while cur:
            if cur.val < x:
                cur_small.next = cur
                cur = cur.next
                cur_small = cur_small.next
                cur_small.next = None
            else:
                cur_large.next = cur
                cur = cur.next
                cur_large = cur_large.next
                cur_large.next = None
        cur_small.next = dummy_large.next
        return dummy_small.next

        
# @lc code=end

