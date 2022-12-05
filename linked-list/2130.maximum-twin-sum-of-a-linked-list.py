''' 
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as 
the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. 
These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1: get the length of the list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        mid = length // 2
        # 2: split the list into two half
        i = 0
        dummy = ListNode(0, head)
        head2 = None
        prev = dummy
        cur = head
        while cur:
            if i == mid:
                prev.next = None
                head2 = cur
                break
            cur = cur.next
            prev = prev.next
            i += 1
        # 3: reverse the second half
        prev = None
        cur = head2
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head2 = prev
        # 4: get the answer
        cur1 = head
        cur2 = head2
        ans = 0
        while cur1:
            ans = max(ans, cur1.val + cur2.val)
            cur1 = cur1.next
            cur2 = cur2.next
        return ans
