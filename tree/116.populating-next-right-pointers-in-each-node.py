#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    '''a simplified version of #117
    '''
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        leftmost = root
        while leftmost:
            cur = leftmost
            prev = None
            while cur:
                if prev is None:
                    leftmost = None
                    if cur.left and cur.right:
                        prev = cur.left
                        leftmost = cur.left
                        prev.next = cur.right
                        prev = prev.next
                        cur = cur.next
                    else:
                        cur = cur.next
                    continue

                prev.next = cur.left
                prev = prev.next
                prev.next = cur.right
                prev = prev.next
                cur = cur.next
        
        return root
# @lc code=end

