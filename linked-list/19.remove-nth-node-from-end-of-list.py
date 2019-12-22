#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.49%)
# Likes:    2267
# Dislikes: 169
# Total Accepted:    473.7K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#

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


class Solution:
    '''operate pointers pre and cur
       do two pass, where the first pass count the size of the list
    '''
    @staticmethod
    def remove(pre, cur):
        '''remove current node'''
        pre.next = cur.next
        cur = cur.next


    @staticmethod
    def count(head):
        counter = 0
        while head is not None:
            counter += 1
            head = head.next
        return counter


    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = Solution.count(head)
        end = size - n

        if end == 0:
            head = head.next
            return head

        index = 1
        pre = head
        cur = head.next        # the current pointer starts at the second element
        while cur is not None: # so it cannot delete the first element in the list
            if index == end:
                Solution.remove(pre, cur)
                break
            pre = cur
            cur = cur.next
            index += 1
        return head


"""
class Solution:
    '''add a dummy node
       operate two pointers slow and fast
       do one pass, 
       don't count the size of the list, but still need to iterate to the list's end
    '''
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head

        for _ in range(n):
            fast = fast.next
        
        while fast is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next
"""

def test1():
    print('test 1')
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    s = Solution()
    l = s.removeNthFromEnd(l1, 2)
    l.print()


def test2():
    print('test 2')
    l1 = ListNode(1)

    s = Solution()
    l = s.removeNthFromEnd(l1, 1)
    try:
        l.print()
    except:
        pass


def test3():
    print('test 3')
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2

    s = Solution()
    l = s.removeNthFromEnd(l1, 2)
    l.print()


if __name__ == '__main__':

    test1()
    test2()
    test3()


# @lc code=end

