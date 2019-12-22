#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (35.49%)
# Likes:    3165
# Dislikes: 208
# Total Accepted:    482.3K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#

from typing import List
import heapq

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        cur = self
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()


class Entry:
    def __init__(self, val, listNode):
        self.val = val
        self.listNode = listNode
    
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    '''Use a heap to maintain the (val, pointer) of each listNode
    '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)  # a dummy node
        last = head
    
        # h = []  # heap
        # for ln in lists:
        #     if ln is not None:
        #         heapq.heappush(h, Entry(ln.val, ln))

        h = [Entry(ln.val, ln) for ln in lists if ln]
        heapq.heapify(h)

        while h:
            # pop the smallest
            entry = heapq.heappop(h)
            val = entry.val
            ln  = entry.listNode
            last.next = ListNode(val)
            last = last.next

            # add a new one
            ln = ln.next
            if ln is not None:
                heapq.heappush(h, Entry(ln.val, ln))
        
        return head.next


def test1():
    inpt_list = []
    l1 = ListNode(1)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l4
    l4.next = l5
    inpt_list.append(l1)

    l1 = ListNode(1)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l3
    l3.next = l4
    inpt_list.append(l1)

    l2 = ListNode(2)
    l6 = ListNode(6)
    l2.next = l6
    inpt_list.append(l2)

    for l in inpt_list:
        l.print()
    
    s = Solution()
    l = s.mergeKLists(inpt_list)
    l.print()



if __name__ == '__main__':
    test1()

# @lc code=end

