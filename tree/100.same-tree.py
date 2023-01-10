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
        elif p is None or q is None:
            return False
        else:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution:
    '''preoder without including None is not unique,
       but including None is unique
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(root: TreeNode) -> list:
            if root is None:
                return ['N']
            return [root.val] + preorder(root.left) + preorder(root.right)
        
        plist = preorder(p)
        qlist = preorder(q)
        for a, b in zip(plist, qlist):
            if a != b:
                return False
        else:
            return True
                
        
# @lc code=end

