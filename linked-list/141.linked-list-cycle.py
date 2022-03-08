#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution2:
    '''puting id(Node) in a set'''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        idset = set()
        cur = head
        while cur:
            if id(cur) in idset:
                return True
            else:
                idset.add(id(cur))
                cur = cur.next
        return False


class Solution3:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while cur:
            if cur.val == 10**6:
                return True
            else:
                cur.val = 10**6
                cur = cur.next
        return False


class Solution:
    '''using two pointers: slow and fast'''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        
# @lc code=end

