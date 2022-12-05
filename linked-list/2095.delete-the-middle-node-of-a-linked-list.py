''' 
You are given the head of a linked list. D
elete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from 
the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        mid = int(length / 2)

        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        i = 0
        while cur:
            if i == mid:
                prev.next = cur.next
                break
            i += 1
            cur = cur.next
            prev = prev.next
        return dummy.next


