#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        nxt = head.next
        remove = False

        while True:
            if nxt is None:
                if remove == True:
                    pre.next = None
                break
            else:  # nxt is not None
                if cur.val == nxt.val:
                    remove = True
                    nxt = nxt.next
                else:  # cur.val != nxt.val
                    if remove == False:
                        pre = cur
                        cur = nxt
                        nxt = nxt.next
                    else:  # remove == True
                        pre.next = nxt
                        cur = nxt
                        nxt = nxt.next
                        remove = False
        return dummy.next

            
        
# @lc code=end

