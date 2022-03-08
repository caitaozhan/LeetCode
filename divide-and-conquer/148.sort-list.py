#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def find_mid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, head1, head2):
        '''assume lists head1 and head2 are already sorted
           return a head to the new merged list
        '''
        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        cur.next = head1 if head1 else head2   # now, either head1 or head2 is None
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:       # empty case
            return None
        if head.next is None:  # single node case
            return head

        mid = self.find_mid(head)
        head = self.sortList(head)
        mid = self.sortList(mid)
        return self.merge(head, mid)

        
# @lc code=end

