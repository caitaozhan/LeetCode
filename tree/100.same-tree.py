#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        else:
            if p.val != q.val:
                return False
            ret1 = self.isSameTree(p.left, q.left)
            ret2 = self.isSameTree(p.right, q.right)
            if ret1 and ret2:
                return True
            else:
                return False
        
        
        
# @lc code=end

