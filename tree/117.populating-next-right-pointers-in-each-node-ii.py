#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = [root]
        while queue:
            new_queue = []
            for i in range(len(queue)):
                # deal with the next of current layer
                if i + 1 < len(queue):
                    queue[i].next = queue[i+1]
                else:
                    queue[i].next = None
            
                # build new layer
                if queue[i].left:
                    new_queue.append(queue[i].left)
                if queue[i].right:
                    new_queue.append(queue[i].right)
            
            queue = new_queue

        return root
        


class Solution:
    '''the prevous solution is a general solution using queues
       this solution is more problem specific
    '''
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root
        while leftmost:
            cur = leftmost
            prev = None
            while cur:
                if prev is None:
                    leftmost = None
                    if cur.left:
                        prev = cur.left
                        leftmost = cur.left
                        if cur.right is None:
                            cur = cur.next
                        else:
                            prev.next = cur.right
                            prev = prev.next
                            cur = cur.next
                    elif cur.right:
                        prev = cur.right
                        leftmost = cur.right
                        cur = cur.next
                    else:
                        cur = cur.next
                    continue
                
                if cur.left is None and cur.right is None:
                    cur = cur.next
                elif cur.left is None and cur.right is not None:
                    prev.next = cur.right
                    prev = prev.next
                    cur = cur.next
                elif cur.left is not None and cur.right is None:
                    prev.next = cur.left
                    prev = prev.next
                    cur = cur.next
                else: # left and right both not None
                    prev.next = cur.left
                    prev = prev.next
                    prev.next = cur.right
                    prev = prev.next
                    cur = cur.next
        
        return root


# @lc code=end

