#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''O(n) space, convert to array
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        n = len(arr)
        left = (n-1) // 2
        right = n // 2
        while left >= 0 and right < n:
            if arr[left] != arr[right]:
                return False
            left -= 1
            right += 1
        return True


class Solution:
    '''O(n) space, recursive (recursive stack is expensive)
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_pointer = head

        def recursive_check(cur: ListNode) -> bool:
            if cur is not None:
                if recursive_check(cur.next) is False:
                    return False
                if cur.val != self.front_pointer.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True
        
        return recursive_check(head)


# @lc code=end

