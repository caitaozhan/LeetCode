#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        first = head
        while cur:
            n += 1
            if n == k:
                first = cur
            cur = cur.next
        
        second = head
        j = 1
        while j != n-k+1:
            second = second.next
            j += 1

        first.val, second.val = second.val, first.val

        return head

        
# @lc code=end

