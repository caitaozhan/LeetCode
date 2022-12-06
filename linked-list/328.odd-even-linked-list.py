#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # step 1: seperate odd and even
        dummy_odd = ListNode(0, head)
        dummy_even = ListNode()
        cur_even = dummy_even
        i = 1
        prev = dummy_odd
        cur = head
        while cur:
            if i % 2 == 1:
                cur = cur.next
                prev = prev.next
                i += 1
            else:
                prev.next = cur.next
                cur_even.next = cur
                cur_even = cur
                cur = cur.next
                cur_even.next = None
                i += 1
        # step 2: link odd and even
        prev.next = dummy_even.next
        return dummy_odd.next




        
# @lc code=end

