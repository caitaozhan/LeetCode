#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''iterative'''
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        nxt = cur.next
        
        while nxt:
            # do the swapping
            pre.next = nxt
            cur.next = nxt.next
            nxt.next = cur

            # update the pointers
            pre = cur
            cur = cur.next
            if cur is None:
                break
            nxt = cur.next

        return dummy.next
    
class Solution:
    '''recursive, more elegant
    '''
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''swap the cur and nxt, and let self.swapPairs(nxt.next) do the rest
           given the head and output the updated head
        '''
        if not head or not head.next:
            return head
        
        cur = head
        nxt = cur.next

        #do the swapping
        cur.next = self.swapPairs(nxt.next)
        nxt.next = cur

        head = nxt
        return head




        
# @lc code=end

