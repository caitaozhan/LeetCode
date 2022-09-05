#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        ans = []
        queue = [root]
        while queue:
            new_queue = []
            cur_layer = []
            for node in queue:
                cur_layer.append(node.val)
                for child in node.children:
                    new_queue.append(child)
            ans.append(cur_layer)
            queue = new_queue
        return ans



# @lc code=end

