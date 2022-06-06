#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import Counter

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count = Counter()
        cura = headA
        curb = headB
        while cura and curb:
            count[cura] += 1
            count[curb] += 1
            if count[cura] == 2:
                return cura
            if count[curb] == 2:
                return curb
            cura = cura.next
            curb = curb.next

        cur = cura or curb
        while cur:
            count[cur] += 1
            if count[cur] == 2:
                return cur
            cur = cur.next
        
        return None


# @lc code=end

