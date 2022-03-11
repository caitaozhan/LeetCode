#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        k = k % length
        if k == 0:
            return head

        dummy = ListNode(0, head)
        slow = head
        fast = head
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        dummy.next = slow.next
        fast.next = head
        slow.next = None

        return dummy.next


# @lc code=end

